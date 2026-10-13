# Pipeline

## Overview

### Available Operations

* [create_crm_pipeline](#create_crm_pipeline) - Create a pipeline
* [get_crm_pipeline](#get_crm_pipeline) - Retrieve a pipeline
* [list_crm_pipelines](#list_crm_pipelines) - List all pipelines
* [patch_crm_pipeline](#patch_crm_pipeline) - Update a pipeline
* [remove_crm_pipeline](#remove_crm_pipeline) - Remove a pipeline
* [update_crm_pipeline](#update_crm_pipeline) - Update a pipeline

## create_crm_pipeline

Create a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="createCrmPipeline" method="post" path="/crm/{connection_id}/pipeline" example="crm_pipeline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pipeline.create_crm_pipeline(request={
        "crm_pipeline": {
            "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
            "deal_probability": 99.0,
            "display_order": 8.0,
            "id": "29f58939-f7f8-4a3c-b30b-5450a91d92ac",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "910995bc-d696-4327-963b-38bfe0d869fb",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-04T10:29:29.743Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-26T00:48:41.394Z"),
        },
        "connection_id": "<id>",
    })

    assert res.crm_pipeline is not None

    # Handle response
    print(res.crm_pipeline)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateCrmPipelineRequest](../../models/operations/createcrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateCrmPipelineResponse](../../models/operations/createcrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_crm_pipeline

Retrieve a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="getCrmPipeline" method="get" path="/crm/{connection_id}/pipeline/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pipeline.get_crm_pipeline(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_pipeline is not None

    # Handle response
    print(res.crm_pipeline)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCrmPipelineRequest](../../models/operations/getcrmpipelinerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetCrmPipelineResponse](../../models/operations/getcrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_pipelines

List all pipelines

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmPipelines" method="get" path="/crm/{connection_id}/pipeline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pipeline.list_crm_pipelines(request={
        "connection_id": "<id>",
    })

    assert res.crm_pipelines is not None

    # Handle response
    print(res.crm_pipelines)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmPipelinesRequest](../../models/operations/listcrmpipelinesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListCrmPipelinesResponse](../../models/operations/listcrmpipelinesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_crm_pipeline

Update a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCrmPipeline" method="patch" path="/crm/{connection_id}/pipeline/{id}" example="crm_pipeline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pipeline.patch_crm_pipeline(request={
        "crm_pipeline": {
            "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
            "deal_probability": 99.0,
            "display_order": 8.0,
            "id": "50bfa9a9-9435-4f13-b4a5-6979f482baae",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "bf41da9d-c06a-4516-98b8-4d792e4ad923",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-04T10:29:29.752Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-26T00:48:41.403Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_pipeline is not None

    # Handle response
    print(res.crm_pipeline)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchCrmPipelineRequest](../../models/operations/patchcrmpipelinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchCrmPipelineResponse](../../models/operations/patchcrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_crm_pipeline

Remove a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCrmPipeline" method="delete" path="/crm/{connection_id}/pipeline/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pipeline.remove_crm_pipeline(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveCrmPipelineRequest](../../models/operations/removecrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveCrmPipelineResponse](../../models/operations/removecrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_crm_pipeline

Update a pipeline

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCrmPipeline" method="put" path="/crm/{connection_id}/pipeline/{id}" example="crm_pipeline" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.pipeline.update_crm_pipeline(request={
        "crm_pipeline": {
            "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
            "deal_probability": 99.0,
            "display_order": 8.0,
            "id": "50bfa9a9-9435-4f13-b4a5-6979f482baae",
            "is_active": True,
            "name": "Small Steel Bacon",
            "stages": [
                {
                    "active": False,
                    "created_at": parse_datetime("2022-12-28T13:45:38.446Z"),
                    "deal_probability": 84.0,
                    "display_order": 72.0,
                    "id": "bf41da9d-c06a-4516-98b8-4d792e4ad923",
                    "is_closed": True,
                    "name": "Veniam.",
                    "updated_at": parse_datetime("2025-10-04T10:29:29.752Z"),
                },
            ],
            "updated_at": parse_datetime("2025-10-26T00:48:41.403Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.crm_pipeline is not None

    # Handle response
    print(res.crm_pipeline)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateCrmPipelineRequest](../../models/operations/updatecrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateCrmPipelineResponse](../../models/operations/updatecrmpipelineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |