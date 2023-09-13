# event

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDEventIDRequest(
    connection_id='unde',
    id='7e152297-510d-4a80-b122-92cc61c2a702',
)

res = s.event.delete_crm_connection_id_event_id(req, operations.DeleteCrmConnectionIDEventIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteCrmConnectionIDEventIDRequest](../../models/operations/deletecrmconnectionideventidrequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.DeleteCrmConnectionIDEventIDSecurity](../../models/operations/deletecrmconnectionideventidsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.DeleteCrmConnectionIDEventIDResponse](../../models/operations/deletecrmconnectionideventidresponse.md)**


## delete_crm_connection_id_event_id_company_company_id

Remove company association from an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDEventIDCompanyCompanyIDRequest(
    company_id='distinctio',
    connection_id='soluta',
    id='97ee102d-a2de-435f-8e01-bf33eaab4540',
)

res = s.event.delete_crm_connection_id_event_id_company_company_id(req, operations.DeleteCrmConnectionIDEventIDCompanyCompanyIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.DeleteCrmConnectionIDEventIDCompanyCompanyIDRequest](../../models/operations/deletecrmconnectionideventidcompanycompanyidrequest.md)   | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |
| `security`                                                                                                                                         | [operations.DeleteCrmConnectionIDEventIDCompanyCompanyIDSecurity](../../models/operations/deletecrmconnectionideventidcompanycompanyidsecurity.md) | :heavy_check_mark:                                                                                                                                 | The security requirements to use for the request.                                                                                                  |


### Response

**[operations.DeleteCrmConnectionIDEventIDCompanyCompanyIDResponse](../../models/operations/deletecrmconnectionideventidcompanycompanyidresponse.md)**


## delete_crm_connection_id_event_id_contact_contact_id

Remove contact association from an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDEventIDContactContactIDRequest(
    connection_id='dolores',
    contact_id='dolorum',
    id='c1704bf1-cc9f-4c61-aae5-eb5f0c492b57',
)

res = s.event.delete_crm_connection_id_event_id_contact_contact_id(req, operations.DeleteCrmConnectionIDEventIDContactContactIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.DeleteCrmConnectionIDEventIDContactContactIDRequest](../../models/operations/deletecrmconnectionideventidcontactcontactidrequest.md)   | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |
| `security`                                                                                                                                         | [operations.DeleteCrmConnectionIDEventIDContactContactIDSecurity](../../models/operations/deletecrmconnectionideventidcontactcontactidsecurity.md) | :heavy_check_mark:                                                                                                                                 | The security requirements to use for the request.                                                                                                  |


### Response

**[operations.DeleteCrmConnectionIDEventIDContactContactIDResponse](../../models/operations/deletecrmconnectionideventidcontactcontactidresponse.md)**


## delete_crm_connection_id_event_id_deal_deal_id

Remove deal association from an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteCrmConnectionIDEventIDDealDealIDRequest(
    connection_id='ut',
    deal_id='incidunt',
    id='d08a2267-aaee-479e-bc71-ad31becb83d2',
)

res = s.event.delete_crm_connection_id_event_id_deal_deal_id(req, operations.DeleteCrmConnectionIDEventIDDealDealIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.DeleteCrmConnectionIDEventIDDealDealIDRequest](../../models/operations/deletecrmconnectionideventiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |
| `security`                                                                                                                             | [operations.DeleteCrmConnectionIDEventIDDealDealIDSecurity](../../models/operations/deletecrmconnectionideventiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                                     | The security requirements to use for the request.                                                                                      |


### Response

**[operations.DeleteCrmConnectionIDEventIDDealDealIDResponse](../../models/operations/deletecrmconnectionideventiddealdealidresponse.md)**


## get_crm_connection_id_event

List all events

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDEventRequest(
    company_id='dolor',
    connection_id='esse',
    contact_id='deleniti',
    deal_id='mollitia',
    limit=8941.65,
    offset=2035.85,
    order='facilis',
    query='sapiente',
    sort='maxime',
    updated_gte=dateutil.parser.parse('2022-10-11').date(),
)

res = s.event.get_crm_connection_id_event(req, operations.GetCrmConnectionIDEventSecurity(
    jwt="",
))

if res.crm_events is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCrmConnectionIDEventRequest](../../models/operations/getcrmconnectionideventrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.GetCrmConnectionIDEventSecurity](../../models/operations/getcrmconnectionideventsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.GetCrmConnectionIDEventResponse](../../models/operations/getcrmconnectionideventresponse.md)**


## get_crm_connection_id_event_id

Retrieve a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmConnectionIDEventIDRequest(
    connection_id='nulla',
    id='9450a986-a495-4bac-b07f-06b28ecc8649',
)

res = s.event.get_crm_connection_id_event_id(req, operations.GetCrmConnectionIDEventIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCrmConnectionIDEventIDRequest](../../models/operations/getcrmconnectionideventidrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetCrmConnectionIDEventIDSecurity](../../models/operations/getcrmconnectionideventidsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetCrmConnectionIDEventIDResponse](../../models/operations/getcrmconnectionideventidresponse.md)**


## patch_crm_connection_id_event_id

Update a event

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDEventIDRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='sunt',
            duration=2261.97,
        ),
        company_ids=[
            'laudantium',
        ],
        contact_ids=[
            'commodi',
        ],
        created_at=dateutil.parser.parse('2021-10-18').date(),
        deal_ids=[
            'qui',
        ],
        email=shared.PropertyCrmEventEmail(
            body='eligendi',
            cc=[
                'perspiciatis',
            ],
            from_='eum',
            subject='sint',
            to=[
                'eligendi',
            ],
        ),
        id='4cc6b788-90a3-4fd3-881d-a10f8c23df93',
        meeting=shared.PropertyCrmEventMeeting(
            description='quae',
            end_at=dateutil.parser.parse('2021-01-28').date(),
            start_at=dateutil.parser.parse('2022-02-09').date(),
            title='Dr.',
        ),
        note=shared.PropertyCrmEventNote(
            description='tempore',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='minima',
            name='Winifred O'Reilly',
            status='numquam',
        ),
        type=shared.CrmEventType.MEETING,
        updated_at=dateutil.parser.parse('2020-08-13').date(),
    ),
    connection_id='sint',
    id='43513772-6d15-4321-b832-a56d69180ff6',
)

res = s.event.patch_crm_connection_id_event_id(req, operations.PatchCrmConnectionIDEventIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchCrmConnectionIDEventIDRequest](../../models/operations/patchcrmconnectionideventidrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.PatchCrmConnectionIDEventIDSecurity](../../models/operations/patchcrmconnectionideventidsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.PatchCrmConnectionIDEventIDResponse](../../models/operations/patchcrmconnectionideventidresponse.md)**


## patch_crm_connection_id_event_id_company_company_id

Associate a company with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDEventIDCompanyCompanyIDRequest(
    company_id='consequatur',
    connection_id='accusamus',
    id='b9a6658e-69a4-4b84-bd38-2dbec75c68c6',
)

res = s.event.patch_crm_connection_id_event_id_company_company_id(req, operations.PatchCrmConnectionIDEventIDCompanyCompanyIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.PatchCrmConnectionIDEventIDCompanyCompanyIDRequest](../../models/operations/patchcrmconnectionideventidcompanycompanyidrequest.md)   | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |
| `security`                                                                                                                                       | [operations.PatchCrmConnectionIDEventIDCompanyCompanyIDSecurity](../../models/operations/patchcrmconnectionideventidcompanycompanyidsecurity.md) | :heavy_check_mark:                                                                                                                               | The security requirements to use for the request.                                                                                                |


### Response

**[operations.PatchCrmConnectionIDEventIDCompanyCompanyIDResponse](../../models/operations/patchcrmconnectionideventidcompanycompanyidresponse.md)**


## patch_crm_connection_id_event_id_contact_contact_id

Associate a contact with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDEventIDContactContactIDRequest(
    connection_id='aut',
    contact_id='nisi',
    id='59468ce3-04d8-4849-bf82-14c337f96bb0',
)

res = s.event.patch_crm_connection_id_event_id_contact_contact_id(req, operations.PatchCrmConnectionIDEventIDContactContactIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.PatchCrmConnectionIDEventIDContactContactIDRequest](../../models/operations/patchcrmconnectionideventidcontactcontactidrequest.md)   | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |
| `security`                                                                                                                                       | [operations.PatchCrmConnectionIDEventIDContactContactIDSecurity](../../models/operations/patchcrmconnectionideventidcontactcontactidsecurity.md) | :heavy_check_mark:                                                                                                                               | The security requirements to use for the request.                                                                                                |


### Response

**[operations.PatchCrmConnectionIDEventIDContactContactIDResponse](../../models/operations/patchcrmconnectionideventidcontactcontactidresponse.md)**


## patch_crm_connection_id_event_id_deal_deal_id

Associate a deal with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmConnectionIDEventIDDealDealIDRequest(
    connection_id='porro',
    deal_id='vel',
    id='9e372db1-344b-4a9f-b8a5-c0ed7aab62e9',
)

res = s.event.patch_crm_connection_id_event_id_deal_deal_id(req, operations.PatchCrmConnectionIDEventIDDealDealIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PatchCrmConnectionIDEventIDDealDealIDRequest](../../models/operations/patchcrmconnectionideventiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `security`                                                                                                                           | [operations.PatchCrmConnectionIDEventIDDealDealIDSecurity](../../models/operations/patchcrmconnectionideventiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                                   | The security requirements to use for the request.                                                                                    |


### Response

**[operations.PatchCrmConnectionIDEventIDDealDealIDResponse](../../models/operations/patchcrmconnectionideventiddealdealidresponse.md)**


## post_crm_connection_id_event

Create a event

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostCrmConnectionIDEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='iusto',
            duration=1323.66,
        ),
        company_ids=[
            'ea',
        ],
        contact_ids=[
            'architecto',
        ],
        created_at=dateutil.parser.parse('2020-10-13').date(),
        deal_ids=[
            'alias',
        ],
        email=shared.PropertyCrmEventEmail(
            body='quod',
            cc=[
                'veniam',
            ],
            from_='corrupti',
            subject='temporibus',
            to=[
                'odit',
            ],
        ),
        id='7b51996b-5b4b-450e-af71-2b7a7ab0344b',
        meeting=shared.PropertyCrmEventMeeting(
            description='inventore',
            end_at=dateutil.parser.parse('2022-11-20').date(),
            start_at=dateutil.parser.parse('2022-08-01').date(),
            title='Ms.',
        ),
        note=shared.PropertyCrmEventNote(
            description='deleniti',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='illum',
            name='Caleb Purdy',
            status='rem',
        ),
        type=shared.CrmEventType.TASK,
        updated_at=dateutil.parser.parse('2022-01-23').date(),
    ),
    connection_id='velit',
)

res = s.event.post_crm_connection_id_event(req, operations.PostCrmConnectionIDEventSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PostCrmConnectionIDEventRequest](../../models/operations/postcrmconnectionideventrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.PostCrmConnectionIDEventSecurity](../../models/operations/postcrmconnectionideventsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.PostCrmConnectionIDEventResponse](../../models/operations/postcrmconnectionideventresponse.md)**


## put_crm_connection_id_event_id

Update a event

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDEventIDRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(
            description='fugiat',
            duration=8660.78,
        ),
        company_ids=[
            'voluptatem',
        ],
        contact_ids=[
            'quod',
        ],
        created_at=dateutil.parser.parse('2020-05-30').date(),
        deal_ids=[
            'dolor',
        ],
        email=shared.PropertyCrmEventEmail(
            body='amet',
            cc=[
                'tenetur',
            ],
            from_='quasi',
            subject='dicta',
            to=[
                'rerum',
            ],
        ),
        id='3e4e080a-a104-4186-ac75-9e02f3702c5c',
        meeting=shared.PropertyCrmEventMeeting(
            description='laudantium',
            end_at=dateutil.parser.parse('2022-08-02').date(),
            start_at=dateutil.parser.parse('2022-05-30').date(),
            title='Mr.',
        ),
        note=shared.PropertyCrmEventNote(
            description='voluptates',
        ),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(
            description='culpa',
            name='Mrs. Leonard Cartwright',
            status='culpa',
        ),
        type=shared.CrmEventType.EMAIL,
        updated_at=dateutil.parser.parse('2022-07-25').date(),
    ),
    connection_id='alias',
    id='7bf375b4-4282-4821-bdb2-f69e59267c71',
)

res = s.event.put_crm_connection_id_event_id(req, operations.PutCrmConnectionIDEventIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutCrmConnectionIDEventIDRequest](../../models/operations/putcrmconnectionideventidrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.PutCrmConnectionIDEventIDSecurity](../../models/operations/putcrmconnectionideventidsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.PutCrmConnectionIDEventIDResponse](../../models/operations/putcrmconnectionideventidresponse.md)**


## put_crm_connection_id_event_id_company_company_id

Associate a company with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDEventIDCompanyCompanyIDRequest(
    company_id='quo',
    connection_id='optio',
    id='8d3cd425-8d03-458a-82c8-08fe2751a204',
)

res = s.event.put_crm_connection_id_event_id_company_company_id(req, operations.PutCrmConnectionIDEventIDCompanyCompanyIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutCrmConnectionIDEventIDCompanyCompanyIDRequest](../../models/operations/putcrmconnectionideventidcompanycompanyidrequest.md)   | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |
| `security`                                                                                                                                   | [operations.PutCrmConnectionIDEventIDCompanyCompanyIDSecurity](../../models/operations/putcrmconnectionideventidcompanycompanyidsecurity.md) | :heavy_check_mark:                                                                                                                           | The security requirements to use for the request.                                                                                            |


### Response

**[operations.PutCrmConnectionIDEventIDCompanyCompanyIDResponse](../../models/operations/putcrmconnectionideventidcompanycompanyidresponse.md)**


## put_crm_connection_id_event_id_contact_contact_id

Associate a contact with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDEventIDContactContactIDRequest(
    connection_id='ducimus',
    contact_id='quod',
    id='0449e143-f961-49bb-bd40-d5a11fa436e6',
)

res = s.event.put_crm_connection_id_event_id_contact_contact_id(req, operations.PutCrmConnectionIDEventIDContactContactIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutCrmConnectionIDEventIDContactContactIDRequest](../../models/operations/putcrmconnectionideventidcontactcontactidrequest.md)   | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |
| `security`                                                                                                                                   | [operations.PutCrmConnectionIDEventIDContactContactIDSecurity](../../models/operations/putcrmconnectionideventidcontactcontactidsecurity.md) | :heavy_check_mark:                                                                                                                           | The security requirements to use for the request.                                                                                            |


### Response

**[operations.PutCrmConnectionIDEventIDContactContactIDResponse](../../models/operations/putcrmconnectionideventidcontactcontactidresponse.md)**


## put_crm_connection_id_event_id_deal_deal_id

Associate a deal with an event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PutCrmConnectionIDEventIDDealDealIDRequest(
    connection_id='sed',
    deal_id='exercitationem',
    id='9233f95c-9d23-4739-bc78-5b5db4f50018',
)

res = s.event.put_crm_connection_id_event_id_deal_deal_id(req, operations.PutCrmConnectionIDEventIDDealDealIDSecurity(
    jwt="",
))

if res.crm_event is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PutCrmConnectionIDEventIDDealDealIDRequest](../../models/operations/putcrmconnectionideventiddealdealidrequest.md)   | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `security`                                                                                                                       | [operations.PutCrmConnectionIDEventIDDealDealIDSecurity](../../models/operations/putcrmconnectionideventiddealdealidsecurity.md) | :heavy_check_mark:                                                                                                               | The security requirements to use for the request.                                                                                |


### Response

**[operations.PutCrmConnectionIDEventIDDealDealIDResponse](../../models/operations/putcrmconnectionideventiddealdealidresponse.md)**

