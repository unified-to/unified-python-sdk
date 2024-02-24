# Event
(*event*)

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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCrmEventRequest(
    connection_id='<value>',
)

res = s.event.create_crm_event(req, operations.CreateCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateCrmEventRequest](../../models/operations/createcrmeventrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.CreateCrmEventSecurity](../../models/operations/createcrmeventsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.CreateCrmEventResponse](../../models/operations/createcrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_crm_event

Retrieve a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCrmEventRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.event.get_crm_event(req, operations.GetCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetCrmEventRequest](../../models/operations/getcrmeventrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.GetCrmEventSecurity](../../models/operations/getcrmeventsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.GetCrmEventResponse](../../models/operations/getcrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_crm_events

List all events

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCrmEventsRequest(
    connection_id='<value>',
)

res = s.event.list_crm_events(req, operations.ListCrmEventsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_events is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListCrmEventsRequest](../../models/operations/listcrmeventsrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.ListCrmEventsSecurity](../../models/operations/listcrmeventssecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.ListCrmEventsResponse](../../models/operations/listcrmeventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_crm_event

Update a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCrmEventRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.event.patch_crm_event(req, operations.PatchCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchCrmEventRequest](../../models/operations/patchcrmeventrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.PatchCrmEventSecurity](../../models/operations/patchcrmeventsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.PatchCrmEventResponse](../../models/operations/patchcrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_crm_event

Remove a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCrmEventRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.event.remove_crm_event(req, operations.RemoveCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveCrmEventRequest](../../models/operations/removecrmeventrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.RemoveCrmEventSecurity](../../models/operations/removecrmeventsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.RemoveCrmEventResponse](../../models/operations/removecrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_crm_event

Update a event

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCrmEventRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.event.update_crm_event(req, operations.UpdateCrmEventSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.crm_event is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateCrmEventRequest](../../models/operations/updatecrmeventrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.UpdateCrmEventSecurity](../../models/operations/updatecrmeventsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.UpdateCrmEventResponse](../../models/operations/updatecrmeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
