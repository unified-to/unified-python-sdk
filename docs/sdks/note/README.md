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
    connection_id='DRAM Liaison',
    id='<ID>',
    ticket_id='Tasty exploit',
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
    connection_id='Account revolutionary',
    limit=2310.88,
    offset=6688.82,
    order='AI',
    query='stanch Investor attitude',
    sort='Cotton',
    ticket_id='Handmade Kia',
    updated_gte=dateutil.parser.isoparse('2022-05-26T17:12:11.333Z'),
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
    connection_id='for',
    id='<ID>',
    ticket_id='female',
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
        agent_id='compress Oganesson',
        created_at=dateutil.parser.isoparse('2022-02-16T08:13:19.991Z'),
        customer_id='demystify',
        description='Fundamental demand-driven workforce',
        id='<ID>',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='Nissan',
    ),
    connection_id='Chicken',
    id='<ID>',
    ticket_id='frictionless convergence officia',
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
        agent_id='Plantation blue',
        created_at=dateutil.parser.isoparse('2021-06-11T06:54:31.529Z'),
        customer_id='asymmetric',
        description='Expanded intermediate attitude',
        id='<ID>',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='naturally',
    ),
    connection_id='Wagon Sulfur',
    ticket_id='digital',
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
        agent_id='SMTP Cis',
        created_at=dateutil.parser.isoparse('2022-07-27T18:14:06.584Z'),
        customer_id='Carolina',
        description='Integrated asymmetric strategy',
        id='<ID>',
        raw=shared.PropertyTicketingNoteRaw(),
        updated_at='Northeast Morocco supposing',
    ),
    connection_id='DNS Fermium',
    id='<ID>',
    ticket_id='Southwest round',
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

