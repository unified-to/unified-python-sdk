# Payslip
(*payslip*)

### Available Operations

* [get_hris_payslip](#get_hris_payslip) - Retrieve a payslip
* [list_hris_payslips](#list_hris_payslips) - List all payslips

## get_hris_payslip

Retrieve a payslip

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.payslip.get_hris_payslip(request=operations.GetHrisPayslipRequest(
    connection_id='<value>',
    id='<id>',
))

if res.hris_payslip is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisPayslipRequest](../../models/operations/gethrispaysliprequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetHrisPayslipResponse](../../models/operations/gethrispayslipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_hris_payslips

List all payslips

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

res = s.payslip.list_hris_payslips(request=operations.ListHrisPayslipsRequest(
    connection_id='<value>',
))

if res.hris_payslips is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisPayslipsRequest](../../models/operations/listhrispayslipsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListHrisPayslipsResponse](../../models/operations/listhrispayslipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
