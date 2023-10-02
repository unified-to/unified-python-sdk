# Event
(*event*)

### Available Operations

* [delete_crm_connection_id_event_id](#delete_crm_connection_id_event_id) - Remove a event
* [get_crm_connection_id_event](#get_crm_connection_id_event) - List all events
* [get_crm_connection_id_event_id](#get_crm_connection_id_event_id) - Retrieve a event
* [patch_crm_connection_id_event_id](#patch_crm_connection_id_event_id) - Update a event
* [post_crm_connection_id_event](#post_crm_connection_id_event) - Create a event
* [put_crm_connection_id_event_id](#put_crm_connection_id_event_id) - Update a event

## delete_crm_connection_id_event_id

Remove a event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDEventIDRequest(
    connection_id='Wooden Latin',
    id='<ID>',
)

res = s.event.delete_crm_connection_id_event_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DeleteCrmConnectionIDEventIDRequest](../../models/operations/deletecrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.DeleteCrmConnectionIDEventIDResponse](../../models/operations/deletecrmconnectionideventidresponse.md)**


## get_crm_connection_id_event

List all events

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

req = operations.GetCrmConnectionIDEventRequest(
    company_id='Zirconium Avon Bedfordshire',
    connection_id='Hybrid grey Ferrari',
    contact_id='Checking Southeast',
    deal_id='Graham till Caesium',
    limit=2928.84,
    offset=5904.77,
    order='furthermore Tricycle Hop',
    query='auxiliary',
    sort='Southeast Bicycle Gorgeous',
    updated_gte=dateutil.parser.isoparse('2023-01-15T23:49:53.643Z'),
)

res = s.event.get_crm_connection_id_event(req)

if res.crm_events is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetCrmConnectionIDEventRequest](../../models/operations/getcrmconnectionideventrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetCrmConnectionIDEventResponse](../../models/operations/getcrmconnectionideventresponse.md)**


## get_crm_connection_id_event_id

Retrieve a event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetCrmConnectionIDEventIDRequest(
    connection_id='Future equalise',
    id='<ID>',
)

res = s.event.get_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCrmConnectionIDEventIDRequest](../../models/operations/getcrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetCrmConnectionIDEventIDResponse](../../models/operations/getcrmconnectionideventidresponse.md)**


## patch_crm_connection_id_event_id

Update a event

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

req = operations.PatchCrmConnectionIDEventIDRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='Optional zero defect function',
            duration=5434.61,
        ),
        company_ids=[
            'silver',
        ],
        contact_ids=[
            'redefine',
        ],
        created_at=dateutil.parser.isoparse('2021-07-21T06:46:42.528Z'),
        deal_ids=[
            'Solutions',
        ],
        email=shared.PropertyCrmEventEmail(
            body='French',
            cc=[
                'Checking',
            ],
            from_='SDD Toyota Northeast',
            subject='Convertible',
            to=[
                'Electronics',
            ],
        ),
        id='<ID>',
        meeting=shared.PropertyCrmEventMeeting(
            description='Monitored mission-critical customer loyalty',
            end_at=dateutil.parser.isoparse('2022-09-22T17:43:00.863Z'),
            start_at=dateutil.parser.isoparse('2023-04-24T06:40:04.926Z'),
            title='Kip Switchable Chicken',
        ),
        note=shared.PropertyCrmEventNote(
            description='Cross-group high-level functionalities',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='Horizontal empowering forecast',
            name='Principal extremely Jast',
            status='striped Concrete Bronze',
        ),
        type=shared.CrmEventType.NOTE,
        updated_at=dateutil.parser.isoparse('2021-02-18T21:34:24.992Z'),
    ),
    connection_id='Dinar benchmark till',
    id='<ID>',
)

res = s.event.patch_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PatchCrmConnectionIDEventIDRequest](../../models/operations/patchcrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PatchCrmConnectionIDEventIDResponse](../../models/operations/patchcrmconnectionideventidresponse.md)**


## post_crm_connection_id_event

Create a event

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

req = operations.PostCrmConnectionIDEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='Visionary bandwidth-monitored hardware',
            duration=9256.02,
        ),
        company_ids=[
            'Kentucky',
        ],
        contact_ids=[
            'Rustic',
        ],
        created_at=dateutil.parser.isoparse('2023-02-12T10:03:55.861Z'),
        deal_ids=[
            'agonizing',
        ],
        email=shared.PropertyCrmEventEmail(
            body='protocol',
            cc=[
                'Ratke',
            ],
            from_='woman',
            subject='East Soft',
            to=[
                'Southeast',
            ],
        ),
        id='<ID>',
        meeting=shared.PropertyCrmEventMeeting(
            description='Streamlined intangible time-frame',
            end_at=dateutil.parser.isoparse('2022-04-18T21:50:55.608Z'),
            start_at=dateutil.parser.isoparse('2021-08-24T14:06:25.626Z'),
            title='violet Synergized blah',
        ),
        note=shared.PropertyCrmEventNote(
            description='Mandatory eco-centric toolset',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='Team-oriented dynamic forecast',
            name='Grocery',
            status='excitedly Bacon',
        ),
        type=shared.CrmEventType.EMAIL,
        updated_at=dateutil.parser.isoparse('2021-09-09T20:12:06.214Z'),
    ),
    connection_id='Progressive',
)

res = s.event.post_crm_connection_id_event(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PostCrmConnectionIDEventRequest](../../models/operations/postcrmconnectionideventrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PostCrmConnectionIDEventResponse](../../models/operations/postcrmconnectionideventresponse.md)**


## put_crm_connection_id_event_id

Update a event

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

req = operations.PutCrmConnectionIDEventIDRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='Re-engineered composite time-frame',
            duration=5444.58,
        ),
        company_ids=[
            'DNS',
        ],
        contact_ids=[
            'Skokie',
        ],
        created_at=dateutil.parser.isoparse('2022-07-05T01:37:36.877Z'),
        deal_ids=[
            'lux',
        ],
        email=shared.PropertyCrmEventEmail(
            body='Hatchback card',
            cc=[
                'Gasoline',
            ],
            from_='Caribbean',
            subject='Account medium',
            to=[
                'copy',
            ],
        ),
        id='<ID>',
        meeting=shared.PropertyCrmEventMeeting(
            description='Inverse optimizing model',
            end_at=dateutil.parser.isoparse('2022-03-21T17:32:41.888Z'),
            start_at=dateutil.parser.isoparse('2022-10-17T10:31:48.119Z'),
            title='male henry Hat',
        ),
        note=shared.PropertyCrmEventNote(
            description='Self-enabling asymmetric functionalities',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='Reduced 4th generation analyzer',
            name='Savings Female nor',
            status='Customer sky',
        ),
        type=shared.CrmEventType.NOTE,
        updated_at=dateutil.parser.isoparse('2023-07-27T14:02:37.510Z'),
    ),
    connection_id='transparent',
    id='<ID>',
)

res = s.event.put_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PutCrmConnectionIDEventIDRequest](../../models/operations/putcrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PutCrmConnectionIDEventIDResponse](../../models/operations/putcrmconnectionideventidresponse.md)**

