# File
(*file*)

### Available Operations

* [delete_crm_connection_id_file_id](#delete_crm_connection_id_file_id) - Remove a file
* [get_crm_connection_id_file](#get_crm_connection_id_file) - List all files
* [get_crm_connection_id_file_id](#get_crm_connection_id_file_id) - Retrieve a file
* [patch_crm_connection_id_file_id](#patch_crm_connection_id_file_id) - Update a file
* [post_crm_connection_id_file](#post_crm_connection_id_file) - Create a file
* [put_crm_connection_id_file_id](#put_crm_connection_id_file_id) - Update a file

## delete_crm_connection_id_file_id

Remove a file

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDFileIDRequest(
    connection_id='adipisci',
    id='febdf676-b720-46da-b750-052a5647edc4',
)

res = s.file.delete_crm_connection_id_file_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteCrmConnectionIDFileIDRequest](../../models/operations/deletecrmconnectionidfileidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteCrmConnectionIDFileIDResponse](../../models/operations/deletecrmconnectionidfileidresponse.md)**


## get_crm_connection_id_file

List all files

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

req = operations.GetCrmConnectionIDFileRequest(
    company_id='sequi',
    connection_id='natus',
    contact_id='saepe',
    deal_id='quibusdam',
    limit=5481.43,
    offset=8071.51,
    order='aliquam',
    query='adipisci',
    sort='explicabo',
    updated_gte=dateutil.parser.isoparse('2022-01-22T06:38:09.253Z'),
)

res = s.file.get_crm_connection_id_file(req)

if res.crm_files is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCrmConnectionIDFileRequest](../../models/operations/getcrmconnectionidfilerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetCrmConnectionIDFileResponse](../../models/operations/getcrmconnectionidfileresponse.md)**


## get_crm_connection_id_file_id

Retrieve a file

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmConnectionIDFileIDRequest(
    connection_id='incidunt',
    id='1240d448-7ac6-493b-94c3-b9d2488d795a',
)

res = s.file.get_crm_connection_id_file_id(req)

if res.crm_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDFileIDRequest](../../models/operations/getcrmconnectionidfileidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetCrmConnectionIDFileIDResponse](../../models/operations/getcrmconnectionidfileidresponse.md)**


## patch_crm_connection_id_file_id

Update a file

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

req = operations.PatchCrmConnectionIDFileIDRequest(
    crm_file=shared.CrmFile(
        active=False,
        activity_id='fuga',
        company_id='incidunt',
        contact_id='aspernatur',
        created_at=dateutil.parser.isoparse('2020-08-02T08:40:50.776Z'),
        deal_id='dolore',
        description='accusantium',
        file_name='corporis',
        file_size=3881.8,
        file_type='laboriosam',
        file_url='omnis',
        id='f69a006d-2124-4945-8819-d7c3b1b41844',
        lead_id='consequatur',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2022-12-09T21:50:08.252Z'),
        user_id='saepe',
    ),
    connection_id='accusantium',
    id='0310d023-dc90-41f5-afd2-a6c44846ae9d',
)

res = s.file.patch_crm_connection_id_file_id(req)

if res.crm_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchCrmConnectionIDFileIDRequest](../../models/operations/patchcrmconnectionidfileidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchCrmConnectionIDFileIDResponse](../../models/operations/patchcrmconnectionidfileidresponse.md)**


## post_crm_connection_id_file

Create a file

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

req = operations.PostCrmConnectionIDFileRequest(
    crm_file=shared.CrmFile(
        active=False,
        activity_id='praesentium',
        company_id='occaecati',
        contact_id='eos',
        created_at=dateutil.parser.isoparse('2022-10-08T19:31:07.425Z'),
        deal_id='nobis',
        description='quos',
        file_name='provident',
        file_size=4099.18,
        file_type='consequuntur',
        file_url='delectus',
        id='4896bf51-e465-42d3-8343-d61778af4912',
        lead_id='numquam',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2022-07-08T10:09:32.871Z'),
        user_id='magni',
    ),
    connection_id='enim',
)

res = s.file.post_crm_connection_id_file(req)

if res.crm_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostCrmConnectionIDFileRequest](../../models/operations/postcrmconnectionidfilerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostCrmConnectionIDFileResponse](../../models/operations/postcrmconnectionidfileresponse.md)**


## put_crm_connection_id_file_id

Update a file

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

req = operations.PutCrmConnectionIDFileIDRequest(
    crm_file=shared.CrmFile(
        active=False,
        activity_id='eveniet',
        company_id='commodi',
        contact_id='magni',
        created_at=dateutil.parser.isoparse('2022-05-23T03:31:28.636Z'),
        deal_id='aut',
        description='occaecati',
        file_name='vero',
        file_size=6231.5,
        file_type='inventore',
        file_url='ipsa',
        id='44a5de59-ac77-4066-b0cf-1cf593260525',
        lead_id='beatae',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2021-10-17T02:29:52.101Z'),
        user_id='ex',
    ),
    connection_id='harum',
    id='b426897d-99a2-4d33-9670-e93ee6cf59f3',
)

res = s.file.put_crm_connection_id_file_id(req)

if res.crm_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutCrmConnectionIDFileIDRequest](../../models/operations/putcrmconnectionidfileidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutCrmConnectionIDFileIDResponse](../../models/operations/putcrmconnectionidfileidresponse.md)**

