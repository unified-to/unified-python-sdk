# Paycode

## Overview

### Available Operations

* [get_hris_paycode](#get_hris_paycode) - Retrieve a paycode
* [list_hris_paycodes](#list_hris_paycodes) - List all paycodes

## get_hris_paycode

Retrieve a paycode

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisPaycode" method="get" path="/hris/{connection_id}/paycode/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.paycode.get_hris_paycode(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_paycode is not None

    # Handle response
    print(res.hris_paycode)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetHrisPaycodeRequest](../../models/operations/gethrispaycoderequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetHrisPaycodeResponse](../../models/operations/gethrispaycoderesponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_paycodes

List all paycodes

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisPaycodes" method="get" path="/hris/{connection_id}/paycode" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.paycode.list_hris_paycodes(request={
        "connection_id": "<id>",
    })

    assert res.hris_paycodes is not None

    # Handle response
    print(res.hris_paycodes)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListHrisPaycodesRequest](../../models/operations/listhrispaycodesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListHrisPaycodesResponse](../../models/operations/listhrispaycodesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |