# Pipeline
(*pipeline*)

### Available Operations

* [delete_crm_connection_id_pipeline_id](#delete_crm_connection_id_pipeline_id) - Remove a pipeline
* [get_crm_connection_id_pipeline](#get_crm_connection_id_pipeline) - List all pipelines
* [get_crm_connection_id_pipeline_id](#get_crm_connection_id_pipeline_id) - Retrieve a pipeline
* [patch_crm_connection_id_pipeline_id](#patch_crm_connection_id_pipeline_id) - Update a pipeline
* [post_crm_connection_id_pipeline](#post_crm_connection_id_pipeline) - Create a pipeline
* [put_crm_connection_id_pipeline_id](#put_crm_connection_id_pipeline_id) - Update a pipeline

## delete_crm_connection_id_pipeline_id

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

req = operations.DeleteCrmConnectionIDPipelineIDRequest(
    connection_id='Customer',
    id='<ID>',
)

res = s.pipeline.delete_crm_connection_id_pipeline_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.DeleteCrmConnectionIDPipelineIDRequest](../../models/operations/deletecrmconnectionidpipelineidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.DeleteCrmConnectionIDPipelineIDResponse](../../models/operations/deletecrmconnectionidpipelineidresponse.md)**


## get_crm_connection_id_pipeline

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

req = operations.GetCrmConnectionIDPipelineRequest(
    connection_id='dirty Awesome Checking',
)

res = s.pipeline.get_crm_connection_id_pipeline(req)

if res.crm_pipelines is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCrmConnectionIDPipelineRequest](../../models/operations/getcrmconnectionidpipelinerequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetCrmConnectionIDPipelineResponse](../../models/operations/getcrmconnectionidpipelineresponse.md)**


## get_crm_connection_id_pipeline_id

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

req = operations.GetCrmConnectionIDPipelineIDRequest(
    connection_id='Tricycle roughly markets',
    id='<ID>',
)

res = s.pipeline.get_crm_connection_id_pipeline_id(req)

if res.crm_pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetCrmConnectionIDPipelineIDRequest](../../models/operations/getcrmconnectionidpipelineidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetCrmConnectionIDPipelineIDResponse](../../models/operations/getcrmconnectionidpipelineidresponse.md)**


## patch_crm_connection_id_pipeline_id

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

req = operations.PatchCrmConnectionIDPipelineIDRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='Bedfordshire bandwidth a',
    id='<ID>',
)

res = s.pipeline.patch_crm_connection_id_pipeline_id(req)

if res.crm_pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PatchCrmConnectionIDPipelineIDRequest](../../models/operations/patchcrmconnectionidpipelineidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PatchCrmConnectionIDPipelineIDResponse](../../models/operations/patchcrmconnectionidpipelineidresponse.md)**


## post_crm_connection_id_pipeline

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

req = operations.PostCrmConnectionIDPipelineRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='Interface alpaca program',
)

res = s.pipeline.post_crm_connection_id_pipeline(req)

if res.crm_pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PostCrmConnectionIDPipelineRequest](../../models/operations/postcrmconnectionidpipelinerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PostCrmConnectionIDPipelineResponse](../../models/operations/postcrmconnectionidpipelineresponse.md)**


## put_crm_connection_id_pipeline_id

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

req = operations.PutCrmConnectionIDPipelineIDRequest(
    crm_pipeline=shared.CrmPipeline(
        raw=shared.PropertyCrmPipelineRaw(),
    ),
    connection_id='back',
    id='<ID>',
)

res = s.pipeline.put_crm_connection_id_pipeline_id(req)

if res.crm_pipeline is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PutCrmConnectionIDPipelineIDRequest](../../models/operations/putcrmconnectionidpipelineidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PutCrmConnectionIDPipelineIDResponse](../../models/operations/putcrmconnectionidpipelineidresponse.md)**

