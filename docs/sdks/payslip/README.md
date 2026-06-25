# Payslip

## Overview

### Available Operations

* [get_hris_payslip2](#get_hris_payslip2) - Retrieve a payslip
* [list_hris_payslips2](#list_hris_payslips2) - List all payslips

## get_hris_payslip2

Retrieve a payslip

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisPayslip2" method="get" path="/hris/{connection_id}/payslip/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payslip.get_hris_payslip2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_payslip is not None

    # Handle response
    print(res.hris_payslip)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisPayslip2Request](../../models/operations/gethrispayslip2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisPayslip2Response](../../models/operations/gethrispayslip2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_payslips2

List all payslips

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisPayslips2" method="get" path="/hris/{connection_id}/payslip" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.payslip.list_hris_payslips2(request={
        "connection_id": "<id>",
    })

    assert res.hris_payslips is not None

    # Handle response
    print(res.hris_payslips)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisPayslips2Request](../../models/operations/listhrispayslips2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisPayslips2Response](../../models/operations/listhrispayslips2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |