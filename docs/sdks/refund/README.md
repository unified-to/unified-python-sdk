# Refund
(*refund*)

### Available Operations

* [get_accounting_refund](#get_accounting_refund) - Retrieve a refund
* [list_accounting_refunds](#list_accounting_refunds) - List all refunds

## get_accounting_refund

Retrieve a refund

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingRefundRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.refund.get_accounting_refund(req, operations.GetAccountingRefundSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_refund is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingRefundRequest](../../models/operations/getaccountingrefundrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetAccountingRefundSecurity](../../models/operations/getaccountingrefundsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetAccountingRefundResponse](../../models/operations/getaccountingrefundresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_refunds

List all refunds

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingRefundsRequest(
    connection_id='<value>',
)

res = s.refund.list_accounting_refunds(req, operations.ListAccountingRefundsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_refunds is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingRefundsRequest](../../models/operations/listaccountingrefundsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.ListAccountingRefundsSecurity](../../models/operations/listaccountingrefundssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.ListAccountingRefundsResponse](../../models/operations/listaccountingrefundsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
