# Customer
(*customer*)

### Available Operations

* [create_ticketing_customer](#create_ticketing_customer) - Create a customer
* [get_ticketing_customer](#get_ticketing_customer) - Retrieve a customer
* [list_ticketing_customers](#list_ticketing_customers) - List all customers
* [patch_ticketing_customer](#patch_ticketing_customer) - Update a customer
* [remove_ticketing_customer](#remove_ticketing_customer) - Remove a customer
* [update_ticketing_customer](#update_ticketing_customer) - Update a customer

## create_ticketing_customer

Create a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateTicketingCustomerRequest(
    connection_id='<value>',
)

res = s.customer.create_ticketing_customer(req, operations.CreateTicketingCustomerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateTicketingCustomerRequest](../../models/operations/createticketingcustomerrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateTicketingCustomerSecurity](../../models/operations/createticketingcustomersecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateTicketingCustomerResponse](../../models/operations/createticketingcustomerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ticketing_customer

Retrieve a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetTicketingCustomerRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.customer.get_ticketing_customer(req, operations.GetTicketingCustomerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetTicketingCustomerRequest](../../models/operations/getticketingcustomerrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetTicketingCustomerSecurity](../../models/operations/getticketingcustomersecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetTicketingCustomerResponse](../../models/operations/getticketingcustomerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ticketing_customers

List all customers

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListTicketingCustomersRequest(
    connection_id='<value>',
)

res = s.customer.list_ticketing_customers(req, operations.ListTicketingCustomersSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_customers is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListTicketingCustomersRequest](../../models/operations/listticketingcustomersrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListTicketingCustomersSecurity](../../models/operations/listticketingcustomerssecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListTicketingCustomersResponse](../../models/operations/listticketingcustomersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_ticketing_customer

Update a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchTicketingCustomerRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.customer.patch_ticketing_customer(req, operations.PatchTicketingCustomerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchTicketingCustomerRequest](../../models/operations/patchticketingcustomerrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchTicketingCustomerSecurity](../../models/operations/patchticketingcustomersecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchTicketingCustomerResponse](../../models/operations/patchticketingcustomerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_ticketing_customer

Remove a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveTicketingCustomerRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.customer.remove_ticketing_customer(req, operations.RemoveTicketingCustomerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveTicketingCustomerRequest](../../models/operations/removeticketingcustomerrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveTicketingCustomerSecurity](../../models/operations/removeticketingcustomersecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveTicketingCustomerResponse](../../models/operations/removeticketingcustomerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_ticketing_customer

Update a customer

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateTicketingCustomerRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.customer.update_ticketing_customer(req, operations.UpdateTicketingCustomerSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.ticketing_customer is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateTicketingCustomerRequest](../../models/operations/updateticketingcustomerrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateTicketingCustomerSecurity](../../models/operations/updateticketingcustomersecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateTicketingCustomerResponse](../../models/operations/updateticketingcustomerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
