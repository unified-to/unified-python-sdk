# Event
(*event*)

### Available Operations

* [delete_crm_connection_id_event_id](#delete_crm_connection_id_event_id) - Remove a event
* [delete_crm_connection_id_event_id_company_company_id](#delete_crm_connection_id_event_id_company_company_id) - Remove company association from an event
* [delete_crm_connection_id_event_id_contact_contact_id](#delete_crm_connection_id_event_id_contact_contact_id) - Remove contact association from an event
* [delete_crm_connection_id_event_id_deal_deal_id](#delete_crm_connection_id_event_id_deal_deal_id) - Remove deal association from an event
* [get_crm_connection_id_event](#get_crm_connection_id_event) - List all events
* [get_crm_connection_id_event_id](#get_crm_connection_id_event_id) - Retrieve a event
* [patch_crm_connection_id_event_id](#patch_crm_connection_id_event_id) - Update a event
* [patch_crm_connection_id_event_id_company_company_id](#patch_crm_connection_id_event_id_company_company_id) - Associate a company with an event
* [patch_crm_connection_id_event_id_contact_contact_id](#patch_crm_connection_id_event_id_contact_contact_id) - Associate a contact with an event
* [patch_crm_connection_id_event_id_deal_deal_id](#patch_crm_connection_id_event_id_deal_deal_id) - Associate a deal with an event
* [post_crm_connection_id_event](#post_crm_connection_id_event) - Create a event
* [put_crm_connection_id_event_id](#put_crm_connection_id_event_id) - Update a event
* [put_crm_connection_id_event_id_company_company_id](#put_crm_connection_id_event_id_company_company_id) - Associate a company with an event
* [put_crm_connection_id_event_id_contact_contact_id](#put_crm_connection_id_event_id_contact_contact_id) - Associate a contact with an event
* [put_crm_connection_id_event_id_deal_deal_id](#put_crm_connection_id_event_id_deal_deal_id) - Associate a deal with an event

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


## delete_crm_connection_id_event_id_company_company_id

Remove company association from an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDEventIDCompanyCompanyIDRequest(
    company_id='Gasoline gentle Japan',
    connection_id='Outdoors',
    id='<ID>',
)

res = s.event.delete_crm_connection_id_event_id_company_company_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.DeleteCrmConnectionIDEventIDCompanyCompanyIDRequest](../../models/operations/deletecrmconnectionideventidcompanycompanyidrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.DeleteCrmConnectionIDEventIDCompanyCompanyIDResponse](../../models/operations/deletecrmconnectionideventidcompanycompanyidresponse.md)**


## delete_crm_connection_id_event_id_contact_contact_id

Remove contact association from an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDEventIDContactContactIDRequest(
    connection_id='lecture Funk',
    contact_id='Bedfordshire Genderqueer',
    id='<ID>',
)

res = s.event.delete_crm_connection_id_event_id_contact_contact_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.DeleteCrmConnectionIDEventIDContactContactIDRequest](../../models/operations/deletecrmconnectionideventidcontactcontactidrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.DeleteCrmConnectionIDEventIDContactContactIDResponse](../../models/operations/deletecrmconnectionideventidcontactcontactidresponse.md)**


## delete_crm_connection_id_event_id_deal_deal_id

Remove deal association from an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteCrmConnectionIDEventIDDealDealIDRequest(
    connection_id='Southeast',
    deal_id='Granite gah Dysprosium',
    id='<ID>',
)

res = s.event.delete_crm_connection_id_event_id_deal_deal_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.DeleteCrmConnectionIDEventIDDealDealIDRequest](../../models/operations/deletecrmconnectionideventiddealdealidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.DeleteCrmConnectionIDEventIDDealDealIDResponse](../../models/operations/deletecrmconnectionideventiddealdealidresponse.md)**


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


## patch_crm_connection_id_event_id_company_company_id

Associate a company with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchCrmConnectionIDEventIDCompanyCompanyIDRequest(
    company_id='quis Operations',
    connection_id='convergence programming',
    id='<ID>',
)

res = s.event.patch_crm_connection_id_event_id_company_company_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.PatchCrmConnectionIDEventIDCompanyCompanyIDRequest](../../models/operations/patchcrmconnectionideventidcompanycompanyidrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.PatchCrmConnectionIDEventIDCompanyCompanyIDResponse](../../models/operations/patchcrmconnectionideventidcompanycompanyidresponse.md)**


## patch_crm_connection_id_event_id_contact_contact_id

Associate a contact with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchCrmConnectionIDEventIDContactContactIDRequest(
    connection_id='gosh',
    contact_id='North Guilder',
    id='<ID>',
)

res = s.event.patch_crm_connection_id_event_id_contact_contact_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.PatchCrmConnectionIDEventIDContactContactIDRequest](../../models/operations/patchcrmconnectionideventidcontactcontactidrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.PatchCrmConnectionIDEventIDContactContactIDResponse](../../models/operations/patchcrmconnectionideventidcontactcontactidresponse.md)**


## patch_crm_connection_id_event_id_deal_deal_id

Associate a deal with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PatchCrmConnectionIDEventIDDealDealIDRequest(
    connection_id='nobis Developer withdrawal',
    deal_id='male connect',
    id='<ID>',
)

res = s.event.patch_crm_connection_id_event_id_deal_deal_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PatchCrmConnectionIDEventIDDealDealIDRequest](../../models/operations/patchcrmconnectionideventiddealdealidrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.PatchCrmConnectionIDEventIDDealDealIDResponse](../../models/operations/patchcrmconnectionideventiddealdealidresponse.md)**


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


## put_crm_connection_id_event_id_company_company_id

Associate a company with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PutCrmConnectionIDEventIDCompanyCompanyIDRequest(
    company_id='Administrator',
    connection_id='Computers',
    id='<ID>',
)

res = s.event.put_crm_connection_id_event_id_company_company_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.PutCrmConnectionIDEventIDCompanyCompanyIDRequest](../../models/operations/putcrmconnectionideventidcompanycompanyidrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.PutCrmConnectionIDEventIDCompanyCompanyIDResponse](../../models/operations/putcrmconnectionideventidcompanycompanyidresponse.md)**


## put_crm_connection_id_event_id_contact_contact_id

Associate a contact with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PutCrmConnectionIDEventIDContactContactIDRequest(
    connection_id='olive',
    contact_id='deposit Bicycle',
    id='<ID>',
)

res = s.event.put_crm_connection_id_event_id_contact_contact_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.PutCrmConnectionIDEventIDContactContactIDRequest](../../models/operations/putcrmconnectionideventidcontactcontactidrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.PutCrmConnectionIDEventIDContactContactIDResponse](../../models/operations/putcrmconnectionideventidcontactcontactidresponse.md)**


## put_crm_connection_id_event_id_deal_deal_id

Associate a deal with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.PutCrmConnectionIDEventIDDealDealIDRequest(
    connection_id='Bloomington',
    deal_id='provided apud Southeast',
    id='<ID>',
)

res = s.event.put_crm_connection_id_event_id_deal_deal_id(req)

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PutCrmConnectionIDEventIDDealDealIDRequest](../../models/operations/putcrmconnectionideventiddealdealidrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.PutCrmConnectionIDEventIDDealDealIDResponse](../../models/operations/putcrmconnectionideventiddealdealidresponse.md)**

