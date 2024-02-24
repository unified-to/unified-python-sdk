# Payout
(*payout*)

### Available Operations

* [get_accounting_payout](#get_accounting_payout) - Retrieve a payout
* [list_accounting_payouts](#list_accounting_payouts) - List all payouts

## get_accounting_payout

Retrieve a payout

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetAccountingPayoutRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.payout.get_accounting_payout(req, operations.GetAccountingPayoutSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payout is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingPayoutRequest](../../models/operations/getaccountingpayoutrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetAccountingPayoutSecurity](../../models/operations/getaccountingpayoutsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetAccountingPayoutResponse](../../models/operations/getaccountingpayoutresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_accounting_payouts

List all payouts

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListAccountingPayoutsRequest(
    connection_id='<value>',
)

res = s.payout.list_accounting_payouts(req, operations.ListAccountingPayoutsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.accounting_payouts is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingPayoutsRequest](../../models/operations/listaccountingpayoutsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.ListAccountingPayoutsSecurity](../../models/operations/listaccountingpayoutssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.ListAccountingPayoutsResponse](../../models/operations/listaccountingpayoutsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
