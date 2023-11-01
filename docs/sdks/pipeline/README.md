# Pipeline
(*.pipeline*)

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
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.CreateCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='string',
)

res = s.pipeline.create_crm_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateCrmPipelineRequest](../../models/operations/createcrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateCrmPipelineResponse](../../models/operations/createcrmpipelineresponse.md)**


## get_crm_pipeline

Retrieve a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmPipelineRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.pipeline.get_crm_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCrmPipelineRequest](../../models/operations/getcrmpipelinerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetCrmPipelineResponse](../../models/operations/getcrmpipelineresponse.md)**


## list_crm_pipelines

List all pipelines

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.ListCrmPipelinesRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.pipeline.list_crm_pipelines(req)

if res.crm_pipelines is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListCrmPipelinesRequest](../../models/operations/listcrmpipelinesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListCrmPipelinesResponse](../../models/operations/listcrmpipelinesresponse.md)**


## patch_crm_pipeline

Update a pipeline

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.pipeline.patch_crm_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchCrmPipelineRequest](../../models/operations/patchcrmpipelinerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PatchCrmPipelineResponse](../../models/operations/patchcrmpipelineresponse.md)**


## remove_crm_pipeline

Remove a pipeline

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.RemoveCrmPipelineRequest(
    connection_id='string',
    id='<ID>',
)

res = s.pipeline.remove_crm_pipeline(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveCrmPipelineRequest](../../models/operations/removecrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RemoveCrmPipelineResponse](../../models/operations/removecrmpipelineresponse.md)**


## update_crm_pipeline

Update a pipeline

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.UpdateCrmPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.pipeline.update_crm_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateCrmPipelineRequest](../../models/operations/updatecrmpipelinerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateCrmPipelineResponse](../../models/operations/updatecrmpipelineresponse.md)**

