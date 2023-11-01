# Event
(*.event*)

### Available Operations

* [create_crm_event](#create_crm_event) - Create a event
* [get_crm_event](#get_crm_event) - Retrieve a event
* [list_crm_events](#list_crm_events) - List all events
* [patch_crm_event](#patch_crm_event) - Update a event
* [remove_crm_event](#remove_crm_event) - Remove a event
* [update_crm_event](#update_crm_event) - Update a event

## create_crm_event

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

req = operations.CreateCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'string',
        ],
        contact_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'string',
            ],
            to=[
                'string',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='string',
)

res = s.event.create_crm_event(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCrmEventRequest](../../models/operations/createcrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateCrmEventResponse](../../models/operations/createcrmeventresponse.md)**


## get_crm_event

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

req = operations.GetCrmEventRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.event.get_crm_event(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCrmEventRequest](../../models/operations/getcrmeventrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetCrmEventResponse](../../models/operations/getcrmeventresponse.md)**


## list_crm_events

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

req = operations.ListCrmEventsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.event.list_crm_events(req)

if res.crm_events is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCrmEventsRequest](../../models/operations/listcrmeventsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListCrmEventsResponse](../../models/operations/listcrmeventsresponse.md)**


## patch_crm_event

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

req = operations.PatchCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'string',
        ],
        contact_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'string',
            ],
            to=[
                'string',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.event.patch_crm_event(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchCrmEventRequest](../../models/operations/patchcrmeventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PatchCrmEventResponse](../../models/operations/patchcrmeventresponse.md)**


## remove_crm_event

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

req = operations.RemoveCrmEventRequest(
    connection_id='string',
    id='<ID>',
)

res = s.event.remove_crm_event(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveCrmEventRequest](../../models/operations/removecrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.RemoveCrmEventResponse](../../models/operations/removecrmeventresponse.md)**


## update_crm_event

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

req = operations.UpdateCrmEventRequest(
    crm_event=shared.CrmEvent(
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'string',
        ],
        contact_ids=[
            'string',
        ],
        deal_ids=[
            'string',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'string',
            ],
            to=[
                'string',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='string',
    id='<ID>',
)

res = s.event.update_crm_event(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCrmEventRequest](../../models/operations/updatecrmeventrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateCrmEventResponse](../../models/operations/updatecrmeventresponse.md)**

