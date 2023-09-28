# Customer
(*customer*)

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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.DeleteTicketingConnectionIDCustomerIDRequest(
    connection_id='Electric Gloves pish',
    id='<ID>',
)

res = s.customer.delete_ticketing_connection_id_customer_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.DeleteTicketingConnectionIDCustomerIDRequest](../../models/operations/deleteticketingconnectionidcustomeridrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.DeleteTicketingConnectionIDCustomerIDResponse](../../models/operations/deleteticketingconnectionidcustomeridresponse.md)**


## get_ticketing_connection_id_customer

List all customers

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

req = operations.GetTicketingConnectionIDCustomerRequest(
    connection_id='SDD because Salad',
    limit=8049.62,
    offset=4323.42,
    order='override',
    query='Rolls 1080p',
    sort='quantifying Southeast Kansas',
    updated_gte=dateutil.parser.isoparse('2023-12-20T19:18:39.254Z'),
)

res = s.customer.get_ticketing_connection_id_customer(req)

if res.ticketing_customers is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTicketingConnectionIDCustomerRequest](../../models/operations/getticketingconnectionidcustomerrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetTicketingConnectionIDCustomerResponse](../../models/operations/getticketingconnectionidcustomerresponse.md)**


## get_ticketing_connection_id_customer_id

Retrieve a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="",
    ),
)

req = operations.GetTicketingConnectionIDCustomerIDRequest(
    connection_id='further Ebert',
    id='<ID>',
)

res = s.customer.get_ticketing_connection_id_customer_id(req)

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetTicketingConnectionIDCustomerIDRequest](../../models/operations/getticketingconnectionidcustomeridrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetTicketingConnectionIDCustomerIDResponse](../../models/operations/getticketingconnectionidcustomeridresponse.md)**


## patch_ticketing_connection_id_customer_id

Update a customer

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

req = operations.PatchTicketingConnectionIDCustomerIDRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2023-01-22T19:33:25.134Z'),
        emails=[
            shared.TicketingEmail(
                email='Ora.Labadie94@yahoo.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='sensitise whiteboard Smyrna',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'Hialeah',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='connect',
                type=shared.TicketingTelephoneType.WORK,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2023-12-28T17:48:45.929Z'),
    ),
    connection_id='Tennessine',
    id='<ID>',
)

res = s.customer.patch_ticketing_connection_id_customer_id(req)

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PatchTicketingConnectionIDCustomerIDRequest](../../models/operations/patchticketingconnectionidcustomeridrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PatchTicketingConnectionIDCustomerIDResponse](../../models/operations/patchticketingconnectionidcustomeridresponse.md)**


## post_ticketing_connection_id_customer

Create a customer

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

req = operations.PostTicketingConnectionIDCustomerRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2022-05-23T15:06:12.012Z'),
        emails=[
            shared.TicketingEmail(
                email='Austin44@yahoo.com',
                type=shared.TicketingEmailType.WORK,
            ),
        ],
        id='<ID>',
        name='Configuration neural',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'engineer',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='Gasoline North gorgeous',
                type=shared.TicketingTelephoneType.FAX,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-10-09T07:25:23.111Z'),
    ),
    connection_id='mole purple',
)

res = s.customer.post_ticketing_connection_id_customer(req)

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.PostTicketingConnectionIDCustomerRequest](../../models/operations/postticketingconnectionidcustomerrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.PostTicketingConnectionIDCustomerResponse](../../models/operations/postticketingconnectionidcustomerresponse.md)**


## put_ticketing_connection_id_customer_id

Update a customer

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

req = operations.PutTicketingConnectionIDCustomerIDRequest(
    ticketing_customer=shared.TicketingCustomer(
        created_at=dateutil.parser.isoparse('2021-04-21T09:25:32.395Z'),
        emails=[
            shared.TicketingEmail(
                email='Shawna42@hotmail.com',
                type=shared.TicketingEmailType.HOME,
            ),
        ],
        id='<ID>',
        name='gray',
        raw=shared.PropertyTicketingCustomerRaw(),
        tags=[
            'Associate',
        ],
        telephones=[
            shared.TicketingTelephone(
                telephone='Sausages ivory Small',
                type=shared.TicketingTelephoneType.MOBILE,
            ),
        ],
        updated_at=dateutil.parser.isoparse('2022-09-01T05:56:15.314Z'),
    ),
    connection_id='mobile Cotton',
    id='<ID>',
)

res = s.customer.put_ticketing_connection_id_customer_id(req)

if res.ticketing_customer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PutTicketingConnectionIDCustomerIDRequest](../../models/operations/putticketingconnectionidcustomeridrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.PutTicketingConnectionIDCustomerIDResponse](../../models/operations/putticketingconnectionidcustomeridresponse.md)**

