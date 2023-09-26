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
    connection_id='laboriosam',
    id='73d522b8-28a9-4030-a60f-024c79b4cc64',
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
    connection_id='eligendi',
    limit=1687.36,
    offset=7276.04,
    order='sequi',
    query='culpa',
    sort='ratione',
    updated_gte=dateutil.parser.isoparse('2022-03-30T02:59:59.063Z'),
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
    connection_id='labore',
    id='88ade62f-6aa5-458a-a5e2-083016ca34bb',
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
        active=False,
        created_at=dateutil.parser.isoparse('2022-01-06T01:33:11.339Z'),
        deal_probability=False,
        display_order=8302.16,
        id='4f62127a-607d-4160-a294-514c3db9ca9f',
        name='Brandy Powlowski',
        raw=shared.PropertyCrmPipelineRaw(),
        updated_at=dateutil.parser.isoparse('2021-03-30T20:29:28.566Z'),
    ),
    connection_id='quos',
    id='78703493-f49a-4a84-a5a3-283279b719d1',
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
        active=False,
        created_at=dateutil.parser.isoparse('2020-05-07T22:58:48.615Z'),
        deal_probability=False,
        display_order=6422.68,
        id='673d86e3-b35e-449a-b135-778ce54cacb0',
        name='Chris Terry',
        raw=shared.PropertyCrmPipelineRaw(),
        updated_at=dateutil.parser.isoparse('2022-09-03T20:01:11.409Z'),
    ),
    connection_id='voluptatem',
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
        active=False,
        created_at=dateutil.parser.isoparse('2022-08-22T17:28:32.263Z'),
        deal_probability=False,
        display_order=6880.36,
        id='acf63b21-5186-4ab5-a3a0-22614315d156',
        name='Victor Mayer',
        raw=shared.PropertyCrmPipelineRaw(),
        updated_at=dateutil.parser.isoparse('2022-11-25T09:18:50.894Z'),
    ),
    connection_id='officia',
    id='fc7186ff-20b7-4a73-9f40-ca0d7657c164',
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

