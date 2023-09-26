# Note
(*note*)

### Available Operations

* [delete_ticketing_connection_id_note_ticket_id_id](#delete_ticketing_connection_id_note_ticket_id_id) - Remove a note
* [get_ticketing_connection_id_note_ticket_id](#get_ticketing_connection_id_note_ticket_id) - List all notes
* [get_ticketing_connection_id_note_ticket_id_id](#get_ticketing_connection_id_note_ticket_id_id) - Retrieve a note
* [patch_ticketing_connection_id_note_ticket_id_id](#patch_ticketing_connection_id_note_ticket_id_id) - Update a note
* [post_ticketing_connection_id_note_ticket_id](#post_ticketing_connection_id_note_ticket_id) - Create a note
* [put_ticketing_connection_id_note_ticket_id_id](#put_ticketing_connection_id_note_ticket_id_id) - Update a note

## delete_ticketing_connection_id_note_ticket_id_id

Remove a note

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteTicketingConnectionIDNoteTicketIDIDRequest(
    connection_id='recusandae',
    id='9085075b-c253-4825-b343-fb0a4e66ea47',
    ticket_id='exercitationem',
)

res = s.note.delete_ticketing_connection_id_note_ticket_id_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.DeleteTicketingConnectionIDNoteTicketIDIDRequest](../../models/operations/deleteticketingconnectionidnoteticketididrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.DeleteTicketingConnectionIDNoteTicketIDIDResponse](../../models/operations/deleteticketingconnectionidnoteticketididresponse.md)**


## get_ticketing_connection_id_note_ticket_id

List all notes

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

req = operations.GetTicketingConnectionIDNoteTicketIDRequest(
    connection_id='molestiae',
    limit=5096.38,
    offset=8540.88,
    order='ab',
    query='voluptate',
    sort='et',
    ticket_id='recusandae',
    updated_gte=dateutil.parser.isoparse('2022-05-19T12:21:22.703Z'),
)

res = s.note.get_ticketing_connection_id_note_ticket_id(req)

if res.ticketing_notes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetTicketingConnectionIDNoteTicketIDRequest](../../models/operations/getticketingconnectionidnoteticketidrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.GetTicketingConnectionIDNoteTicketIDResponse](../../models/operations/getticketingconnectionidnoteticketidresponse.md)**


## get_ticketing_connection_id_note_ticket_id_id

Retrieve a note

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetTicketingConnectionIDNoteTicketIDIDRequest(
    connection_id='eius',
    id='1818fc67-9b6b-42f2-9359-b855d015b62c',
    ticket_id='quos',
)

res = s.note.get_ticketing_connection_id_note_ticket_id_id(req)

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetTicketingConnectionIDNoteTicketIDIDRequest](../../models/operations/getticketingconnectionidnoteticketididrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetTicketingConnectionIDNoteTicketIDIDResponse](../../models/operations/getticketingconnectionidnoteticketididresponse.md)**


## patch_ticketing_connection_id_note_ticket_id_id

Update a note

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

req = operations.PatchTicketingConnectionIDNoteTicketIDIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='cum',
        created_at=dateutil.parser.isoparse('2022-07-23T08:55:47.914Z'),
        customer_id='dolorum',
        description='amet',
        id='8a8a88c1-4420-40c2-8aeb-1ae1ecf8c349',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='modi',
    ),
    connection_id='commodi',
    id='bba7a05a-8b4a-49ec-9b36-88cca3632727',
    ticket_id='iure',
)

res = s.note.patch_ticketing_connection_id_note_ticket_id_id(req)

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.PatchTicketingConnectionIDNoteTicketIDIDRequest](../../models/operations/patchticketingconnectionidnoteticketididrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.PatchTicketingConnectionIDNoteTicketIDIDResponse](../../models/operations/patchticketingconnectionidnoteticketididresponse.md)**


## post_ticketing_connection_id_note_ticket_id

Create a note

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

req = operations.PostTicketingConnectionIDNoteTicketIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='sit',
        created_at=dateutil.parser.isoparse('2021-04-03T18:27:00.342Z'),
        customer_id='vel',
        description='autem',
        id='e97e0541-0334-47d7-8ff2-491145fab9e5',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='perspiciatis',
    ),
    connection_id='laborum',
    ticket_id='incidunt',
)

res = s.note.post_ticketing_connection_id_note_ticket_id(req)

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PostTicketingConnectionIDNoteTicketIDRequest](../../models/operations/postticketingconnectionidnoteticketidrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.PostTicketingConnectionIDNoteTicketIDResponse](../../models/operations/postticketingconnectionidnoteticketidresponse.md)**


## put_ticketing_connection_id_note_ticket_id_id

Update a note

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

req = operations.PutTicketingConnectionIDNoteTicketIDIDRequest(
    ticketing_note=shared.TicketingNote(
        agent_id='fuga',
        created_at=dateutil.parser.isoparse('2022-05-09T22:54:29.590Z'),
        customer_id='amet',
        description='nisi',
        id='664eaa6b-f2ff-414e-8c1b-352accedacc5',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='consequuntur',
    ),
    connection_id='qui',
    id='7814eca0-16bc-441e-a134-2d4104a25ef7',
    ticket_id='quasi',
)

res = s.note.put_ticketing_connection_id_note_ticket_id_id(req)

if res.ticketing_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PutTicketingConnectionIDNoteTicketIDIDRequest](../../models/operations/putticketingconnectionidnoteticketididrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PutTicketingConnectionIDNoteTicketIDIDResponse](../../models/operations/putticketingconnectionidnoteticketididresponse.md)**

