# Pipeline
(*pipeline*)

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

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCrmPipelineRequest(
    connection_id='<value>',
)

res = s.pipeline.create_crm_pipeline(req, operations.CreateCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateCrmPipelineRequest](../../models/operations/createcrmpipelinerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateCrmPipelineSecurity](../../models/operations/createcrmpipelinesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateCrmPipelineResponse](../../models/operations/createcrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_crm_pipeline

Retrieve a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmPipelineRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.pipeline.get_crm_pipeline(req, operations.GetCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCrmPipelineRequest](../../models/operations/getcrmpipelinerequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetCrmPipelineSecurity](../../models/operations/getcrmpipelinesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetCrmPipelineResponse](../../models/operations/getcrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_crm_pipelines

List all pipelines

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCrmPipelinesRequest(
    connection_id='<value>',
)

res = s.pipeline.list_crm_pipelines(req, operations.ListCrmPipelinesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipelines is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCrmPipelinesRequest](../../models/operations/listcrmpipelinesrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListCrmPipelinesSecurity](../../models/operations/listcrmpipelinessecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListCrmPipelinesResponse](../../models/operations/listcrmpipelinesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_crm_pipeline

Update a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmPipelineRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.pipeline.patch_crm_pipeline(req, operations.PatchCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchCrmPipelineRequest](../../models/operations/patchcrmpipelinerequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PatchCrmPipelineSecurity](../../models/operations/patchcrmpipelinesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PatchCrmPipelineResponse](../../models/operations/patchcrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_crm_pipeline

Remove a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCrmPipelineRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.pipeline.remove_crm_pipeline(req, operations.RemoveCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveCrmPipelineRequest](../../models/operations/removecrmpipelinerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RemoveCrmPipelineSecurity](../../models/operations/removecrmpipelinesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RemoveCrmPipelineResponse](../../models/operations/removecrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_crm_pipeline

Update a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCrmPipelineRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.pipeline.update_crm_pipeline(req, operations.UpdateCrmPipelineSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateCrmPipelineRequest](../../models/operations/updatecrmpipelinerequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateCrmPipelineSecurity](../../models/operations/updatecrmpipelinesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateCrmPipelineResponse](../../models/operations/updatecrmpipelineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
