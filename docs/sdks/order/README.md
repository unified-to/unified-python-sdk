# Order

## Overview

### Available Operations

* [create_accounting_order2](#create_accounting_order2) - Create an order
* [get_accounting_order2](#get_accounting_order2) - Retrieve an order
* [list_accounting_orders2](#list_accounting_orders2) - List all orders
* [patch_accounting_order2](#patch_accounting_order2) - Update an order
* [patch_assessment_order2](#patch_assessment_order2) - Update an order
* [remove_accounting_order2](#remove_accounting_order2) - Remove an order
* [update_accounting_order2](#update_accounting_order2) - Update an order
* [update_assessment_order2](#update_assessment_order2) - Update an order

## create_accounting_order2

Create an order

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingOrder2" method="post" path="/accounting/{connection_id}/order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.create_accounting_order2(request={
        "accounting_order": {},
        "connection_id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateAccountingOrder2Request](../../models/operations/createaccountingorder2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateAccountingOrder2Response](../../models/operations/createaccountingorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_order2

Retrieve an order

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingOrder2" method="get" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.get_accounting_order2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetAccountingOrder2Request](../../models/operations/getaccountingorder2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetAccountingOrder2Response](../../models/operations/getaccountingorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_orders2

List all orders

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingOrders2" method="get" path="/accounting/{connection_id}/order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.list_accounting_orders2(request={
        "connection_id": "<id>",
    })

    assert res.accounting_orders is not None

    # Handle response
    print(res.accounting_orders)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListAccountingOrders2Request](../../models/operations/listaccountingorders2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListAccountingOrders2Response](../../models/operations/listaccountingorders2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_order2

Update an order

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingOrder2" method="patch" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.patch_accounting_order2(request={
        "accounting_order": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchAccountingOrder2Request](../../models/operations/patchaccountingorder2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchAccountingOrder2Response](../../models/operations/patchaccountingorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_assessment_order2

Update an order

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAssessmentOrder2" method="patch" path="/assessment/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.patch_assessment_order2(request={
        "assessment_order": {
            "connection_id": "<id>",
            "workspace_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchAssessmentOrder2Request](../../models/operations/patchassessmentorder2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchAssessmentOrder2Response](../../models/operations/patchassessmentorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_order2

Remove an order

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingOrder2" method="delete" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.remove_accounting_order2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveAccountingOrder2Request](../../models/operations/removeaccountingorder2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveAccountingOrder2Response](../../models/operations/removeaccountingorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_order2

Update an order

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingOrder2" method="put" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.update_accounting_order2(request={
        "accounting_order": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateAccountingOrder2Request](../../models/operations/updateaccountingorder2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateAccountingOrder2Response](../../models/operations/updateaccountingorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_assessment_order2

Update an order

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAssessmentOrder2" method="put" path="/assessment/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.update_assessment_order2(request={
        "assessment_order": {
            "connection_id": "<id>",
            "workspace_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateAssessmentOrder2Request](../../models/operations/updateassessmentorder2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateAssessmentOrder2Response](../../models/operations/updateassessmentorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |