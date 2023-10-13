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
    pass
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
    connection_id='Zirconium Avon Bedfordshire',
)

res = s.event.get_crm_connection_id_event(req)

if res.crm_events is not None:
    # handle response
    pass
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
    pass
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
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'parse',
        ],
        contact_ids=[
            'intranet',
        ],
        deal_ids=[
            'silver',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'redefine',
            ],
            to=[
                'Baby',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='Steel',
    id='<ID>',
)

res = s.event.patch_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
    pass
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
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'carburize',
        ],
        contact_ids=[
            'SDR',
        ],
        deal_ids=[
            'Kentucky',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'Rustic',
            ],
            to=[
                'male',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='Hat',
)

res = s.event.post_crm_connection_id_event(req)

if res.crm_event is not None:
    # handle response
    pass
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
        call=shared.PropertyCrmEventCall(),
        company_ids=[
            'Iron',
        ],
        contact_ids=[
            'marshmallow',
        ],
        deal_ids=[
            'DNS',
        ],
        email=shared.PropertyCrmEventEmail(
            cc=[
                'Skokie',
            ],
            to=[
                'calculating',
            ],
        ),
        meeting=shared.PropertyCrmEventMeeting(),
        note=shared.PropertyCrmEventNote(),
        raw=shared.PropertyCrmEventRaw(),
        task=shared.PropertyCrmEventTask(),
    ),
    connection_id='Blues firewall engineer',
    id='<ID>',
)

res = s.event.put_crm_connection_id_event_id(req)

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PutCrmConnectionIDEventIDRequest](../../models/operations/putcrmconnectionideventidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PutCrmConnectionIDEventIDResponse](../../models/operations/putcrmconnectionideventidresponse.md)**

