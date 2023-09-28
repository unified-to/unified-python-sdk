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
    connection_id='Bicycle',
    id='<ID>',
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
    company_id='reboot',
    connection_id='customise far',
    contact_id='Electronic proactive',
    deal_id='withdrawal deposit Gloves',
    limit=1588.79,
    offset=3754.81,
    order='Implemented fairly meh',
    query='FTP Producer',
    sort='soprano deliverables',
    updated_gte=dateutil.parser.isoparse('2022-03-02T03:00:09.711Z'),
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
    connection_id='Bicycle',
    id='<ID>',
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
        activity_id='duh Handmade harness',
        company_id='CFP',
        contact_id='unaware yellow generating',
        created_at=dateutil.parser.isoparse('2021-05-04T04:54:33.785Z'),
        deal_id='channels SUV',
        description='De-engineered didactic hardware',
        file_name='metical_silver_yellow.html',
        file_size=6861.53,
        file_type='video',
        file_url='navigate Funk',
        id='<ID>',
        lead_id='internal',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2023-02-21T13:46:42.012Z'),
        user_id='Interactions',
    ),
    connection_id='Handcrafted',
    id='<ID>',
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
        activity_id='tan impedit Pickup',
        company_id='Manager',
        contact_id='Florida Shoes East',
        created_at=dateutil.parser.isoparse('2023-01-08T11:37:24.708Z'),
        deal_id='Agent',
        description='Multi-lateral well-modulated portal',
        file_name='panel_city.wav',
        file_size=1401.73,
        file_type='application',
        file_url='for Chips under',
        id='<ID>',
        lead_id='abaft Checking',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2023-02-25T09:46:59.608Z'),
        user_id='Mexico withdrawal',
    ),
    connection_id='national Lead',
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
        activity_id='Cotton',
        company_id='Northeast',
        contact_id='Computer',
        created_at=dateutil.parser.isoparse('2021-04-09T13:10:01.367Z'),
        deal_id='toward confiscate East',
        description='Devolved upward-trending matrices',
        file_name='generation_tactics.wav',
        file_size=4770.09,
        file_type='audio',
        file_url='framework azure Metal',
        id='<ID>',
        lead_id='ampere costume',
        raw=shared.PropertyCrmFileRaw(),
        updated_at=dateutil.parser.isoparse('2023-05-15T05:04:24.130Z'),
        user_id='Research payment',
    ),
    connection_id='East Associate Mazda',
    id='<ID>',
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

