# Payroll

## Overview

### Available Operations

* [get_hris_payroll](#get_hris_payroll) - Retrieve a payroll
* [list_hris_payrolls](#list_hris_payrolls) - List all payrolls

## get_hris_payroll

Retrieve a payroll

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisPayroll" method="get" path="/hris/{connection_id}/payroll/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payroll.get_hris_payroll(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_payroll is not None

    # Handle response
    print(res.hris_payroll)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisPayrollRequest](../../models/operations/gethrispayrollrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisPayrollResponse](../../models/operations/gethrispayrollresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_payrolls

List all payrolls

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisPayrolls" method="get" path="/hris/{connection_id}/payroll" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payroll.list_hris_payrolls(request={
        "connection_id": "<id>",
    })

    assert res.hris_payrolls is not None

    # Handle response
    print(res.hris_payrolls)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisPayrollsRequest](../../models/operations/listhrispayrollsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisPayrollsResponse](../../models/operations/listhrispayrollsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |