# customer

### Available Operations

* [delete_ticketing_connection_id_customer_id](#delete_ticketing_connection_id_customer_id) - Remove a customer
* [get_ticketing_connection_id_customer](#get_ticketing_connection_id_customer) - List all customers
* [get_ticketing_connection_id_customer_id](#get_ticketing_connection_id_customer_id) - Retrieve a customer
* [patch_ticketing_connection_id_customer_id](#patch_ticketing_connection_id_customer_id) - Update a customer
* [post_ticketing_connection_id_customer](#post_ticketing_connection_id_customer) - Create a customer
* [put_ticketing_connection_id_customer_id](#put_ticketing_connection_id_customer_id) - Update a customer

## delete_ticketing_connection_id_customer_id

Remove a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.DeleteTicketingConnectionIDCustomerIDRequest(
    connection_id='nulla',
    id='acd38ed0-dc67-41dc-bf1e-3af15920c90d',
)

res = s.customer.delete_ticketing_connection_id_customer_id(req, operations.DeleteTicketingConnectionIDCustomerIDSecurity(
    jwt="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.DeleteTicketingConnectionIDCustomerIDRequest](../../models/operations/deleteticketingconnectionidcustomeridrequest.md)   | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `security`                                                                                                                           | [operations.DeleteTicketingConnectionIDCustomerIDSecurity](../../models/operations/deleteticketingconnectionidcustomeridsecurity.md) | :heavy_check_mark:                                                                                                                   | The security requirements to use for the request.                                                                                    |


### Response

**[operations.DeleteTicketingConnectionIDCustomerIDResponse](../../models/operations/deleteticketingconnectionidcustomeridresponse.md)**


## get_ticketing_connection_id_customer

List all customers

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDCustomerRequest(
    connection_id='ab',
    limit=7414.54,
    offset=2975.19,
    order='natus',
    query='aperiam',
    sort='dicta',
    updated_gte=dateutil.parser.isoparse('2022-06-25T18:37:10.473Z'),
)

res = s.customer.get_ticketing_connection_id_customer(req, operations.GetTicketingConnectionIDCustomerSecurity(
    jwt="",
))

if res.ticketing_customers is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GetTicketingConnectionIDCustomerRequest](../../models/operations/getticketingconnectionidcustomerrequest.md)   | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `security`                                                                                                                 | [operations.GetTicketingConnectionIDCustomerSecurity](../../models/operations/getticketingconnectionidcustomersecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.GetTicketingConnectionIDCustomerResponse](../../models/operations/getticketingconnectionidcustomerresponse.md)**


## get_ticketing_connection_id_customer_id

Retrieve a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingConnectionIDCustomerIDRequest(
    connection_id='harum',
    id='d89c8a32-639d-4a5b-bb69-02b881a94f64',
)

res = s.customer.get_ticketing_connection_id_customer_id(req, operations.GetTicketingConnectionIDCustomerIDSecurity(
    jwt="",
))

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetTicketingConnectionIDCustomerIDRequest](../../models/operations/getticketingconnectionidcustomeridrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.GetTicketingConnectionIDCustomerIDSecurity](../../models/operations/getticketingconnectionidcustomeridsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.GetTicketingConnectionIDCustomerIDResponse](../../models/operations/getticketingconnectionidcustomeridresponse.md)**


## patch_ticketing_connection_id_customer_id

Update a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PatchTicketingConnectionIDCustomerIDRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2022-08-10T23:28:30.532Z'),
        emails=[
            shared.TicketingEmail(
                email='Donny_OKeefe@yahoo.com',
                type=shared.TicketingEmailType.WORK,
            ),
        ],
        id='af8c691d-732d-49fb-af94-76a2ae8dcc50',
        name='Clifton Nicolas',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'dicta',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='eos',
                type=shared.TicketingTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-10-15T18:32:49.022Z'),
    ),
    connection_id='voluptate',
    id='84893075-0a00-4e96-aec7-36d43194398c',
)

res = s.customer.patch_ticketing_connection_id_customer_id(req, operations.PatchTicketingConnectionIDCustomerIDSecurity(
    jwt="",
))

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PatchTicketingConnectionIDCustomerIDRequest](../../models/operations/patchticketingconnectionidcustomeridrequest.md)   | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `security`                                                                                                                         | [operations.PatchTicketingConnectionIDCustomerIDSecurity](../../models/operations/patchticketingconnectionidcustomeridsecurity.md) | :heavy_check_mark:                                                                                                                 | The security requirements to use for the request.                                                                                  |


### Response

**[operations.PatchTicketingConnectionIDCustomerIDResponse](../../models/operations/patchticketingconnectionidcustomeridresponse.md)**


## post_ticketing_connection_id_customer

Create a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PostTicketingConnectionIDCustomerRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2022-06-17T14:22:05.995Z'),
        emails=[
            shared.TicketingEmail(
                email='Nils22@gmail.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='8ed3d3ab-7ca3-4c5c-a864-9a70cfd5d698',
        name='Rudy Kirlin III',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'magnam',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='ad',
                type=shared.TicketingTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-07-25T05:00:03.848Z'),
    ),
    connection_id='voluptate',
)

res = s.customer.post_ticketing_connection_id_customer(req, operations.PostTicketingConnectionIDCustomerSecurity(
    jwt="",
))

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PostTicketingConnectionIDCustomerRequest](../../models/operations/postticketingconnectionidcustomerrequest.md)   | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `security`                                                                                                                   | [operations.PostTicketingConnectionIDCustomerSecurity](../../models/operations/postticketingconnectionidcustomersecurity.md) | :heavy_check_mark:                                                                                                           | The security requirements to use for the request.                                                                            |


### Response

**[operations.PostTicketingConnectionIDCustomerResponse](../../models/operations/postticketingconnectionidcustomerresponse.md)**


## put_ticketing_connection_id_customer_id

Update a customer

### Example Usage

```python
import unified_to
import dateutil.parser
from unified_to.models import operations, shared

s = unified_to.UnifiedTo()

req = operations.PutTicketingConnectionIDCustomerIDRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2022-09-26T16:23:23.443Z'),
        emails=[
            shared.TicketingEmail(
                email='Shanny.Padberg@yahoo.com',
                type=shared.TicketingEmailType.OTHER,
            ),
        ],
        id='492ed14b-8a2c-4195-8545-e955dcc185ea',
        name='Miss Lindsay Adams',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'cumque',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='quaerat',
                type=shared.TicketingTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2021-05-15T13:31:18.582Z'),
    ),
    connection_id='explicabo',
    id='daa784ab-a3d2-430e-9f73-811a115382bd',
)

res = s.customer.put_ticketing_connection_id_customer_id(req, operations.PutTicketingConnectionIDCustomerIDSecurity(
    jwt="",
))

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PutTicketingConnectionIDCustomerIDRequest](../../models/operations/putticketingconnectionidcustomeridrequest.md)   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.PutTicketingConnectionIDCustomerIDSecurity](../../models/operations/putticketingconnectionidcustomeridsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.PutTicketingConnectionIDCustomerIDResponse](../../models/operations/putticketingconnectionidcustomeridresponse.md)**

