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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetAccountingRefundRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.refund.get_accounting_refund(req)

if res.accounting_refund is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetAccountingRefundRequest](../../models/operations/getaccountingrefundrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListAccountingRefundsRequest(
    connection_id='<value>',
)

res = s.refund.list_accounting_refunds(req)

if res.accounting_refunds is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListAccountingRefundsRequest](../../models/operations/listaccountingrefundsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.ListAccountingRefundsResponse](../../models/operations/listaccountingrefundsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
