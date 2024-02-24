# Note
(*note*)

### Available Operations

* [create_ticketing_note](#create_ticketing_note) - Create a note
* [get_ticketing_note](#get_ticketing_note) - Retrieve a note
* [list_ticketing_notes](#list_ticketing_notes) - List all notes
* [patch_ticketing_note](#patch_ticketing_note) - Update a note
* [remove_ticketing_note](#remove_ticketing_note) - Remove a note
* [update_ticketing_note](#update_ticketing_note) - Update a note

## create_ticketing_note

Create a note

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateTicketingNoteRequest(
    connection_id='<value>',
)

res = s.note.create_ticketing_note(req, operations.CreateTicketingNoteSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateTicketingNoteRequest](../../models/operations/createticketingnoterequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.CreateTicketingNoteSecurity](../../models/operations/createticketingnotesecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.CreateTicketingNoteResponse](../../models/operations/createticketingnoteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ticketing_note

Retrieve a note

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingNoteRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.note.get_ticketing_note(req, operations.GetTicketingNoteSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetTicketingNoteRequest](../../models/operations/getticketingnoterequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.GetTicketingNoteSecurity](../../models/operations/getticketingnotesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.GetTicketingNoteResponse](../../models/operations/getticketingnoteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ticketing_notes

List all notes

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListTicketingNotesRequest(
    connection_id='<value>',
)

res = s.note.list_ticketing_notes(req, operations.ListTicketingNotesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_notes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListTicketingNotesRequest](../../models/operations/listticketingnotesrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ListTicketingNotesSecurity](../../models/operations/listticketingnotessecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ListTicketingNotesResponse](../../models/operations/listticketingnotesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ticketing_note

Update a note

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchTicketingNoteRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.note.patch_ticketing_note(req, operations.PatchTicketingNoteSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchTicketingNoteRequest](../../models/operations/patchticketingnoterequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.PatchTicketingNoteSecurity](../../models/operations/patchticketingnotesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.PatchTicketingNoteResponse](../../models/operations/patchticketingnoteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ticketing_note

Remove a note

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveTicketingNoteRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.note.remove_ticketing_note(req, operations.RemoveTicketingNoteSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveTicketingNoteRequest](../../models/operations/removeticketingnoterequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.RemoveTicketingNoteSecurity](../../models/operations/removeticketingnotesecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.RemoveTicketingNoteResponse](../../models/operations/removeticketingnoteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ticketing_note

Update a note

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateTicketingNoteRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.note.update_ticketing_note(req, operations.UpdateTicketingNoteSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_note is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateTicketingNoteRequest](../../models/operations/updateticketingnoterequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.UpdateTicketingNoteSecurity](../../models/operations/updateticketingnotesecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.UpdateTicketingNoteResponse](../../models/operations/updateticketingnoteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
