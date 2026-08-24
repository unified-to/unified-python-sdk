# Paymentterm

## Overview

### Available Operations

* [create_accounting_paymentterm](#create_accounting_paymentterm) - Create a paymentterm
* [get_accounting_paymentterm](#get_accounting_paymentterm) - Retrieve a paymentterm
* [list_accounting_paymentterms](#list_accounting_paymentterms) - List all paymentterms
* [patch_accounting_paymentterm](#patch_accounting_paymentterm) - Update a paymentterm
* [remove_accounting_paymentterm](#remove_accounting_paymentterm) - Remove a paymentterm
* [update_accounting_paymentterm](#update_accounting_paymentterm) - Update a paymentterm

## create_accounting_paymentterm

Create a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingPaymentterm" method="post" path="/accounting/{connection_id}/paymentterm" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.paymentterm.create_accounting_paymentterm(request={
        "accounting_paymentterm": {},
        "connection_id": "<id>",
    })

    assert res.accounting_paymentterm is not None

    # Handle response
    print(res.accounting_paymentterm)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateAccountingPaymenttermRequest](../../models/operations/createaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.CreateAccountingPaymenttermResponse](../../models/operations/createaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_paymentterm

Retrieve a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingPaymentterm" method="get" path="/accounting/{connection_id}/paymentterm/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.paymentterm.get_accounting_paymentterm(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_paymentterm is not None

    # Handle response
    print(res.accounting_paymentterm)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAccountingPaymenttermRequest](../../models/operations/getaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetAccountingPaymenttermResponse](../../models/operations/getaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_paymentterms

List all paymentterms

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingPaymentterms" method="get" path="/accounting/{connection_id}/paymentterm" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.paymentterm.list_accounting_paymentterms(request={
        "connection_id": "<id>",
    })

    assert res.accounting_paymentterms is not None

    # Handle response
    print(res.accounting_paymentterms)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingPaymenttermsRequest](../../models/operations/listaccountingpaymenttermsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAccountingPaymenttermsResponse](../../models/operations/listaccountingpaymenttermsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_paymentterm

Update a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingPaymentterm" method="patch" path="/accounting/{connection_id}/paymentterm/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.paymentterm.patch_accounting_paymentterm(request={
        "accounting_paymentterm": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_paymentterm is not None

    # Handle response
    print(res.accounting_paymentterm)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchAccountingPaymenttermRequest](../../models/operations/patchaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.PatchAccountingPaymenttermResponse](../../models/operations/patchaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_paymentterm

Remove a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingPaymentterm" method="delete" path="/accounting/{connection_id}/paymentterm/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.paymentterm.remove_accounting_paymentterm(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RemoveAccountingPaymenttermRequest](../../models/operations/removeaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.RemoveAccountingPaymenttermResponse](../../models/operations/removeaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_paymentterm

Update a paymentterm

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingPaymentterm" method="put" path="/accounting/{connection_id}/paymentterm/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.paymentterm.update_accounting_paymentterm(request={
        "accounting_paymentterm": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_paymentterm is not None

    # Handle response
    print(res.accounting_paymentterm)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateAccountingPaymenttermRequest](../../models/operations/updateaccountingpaymenttermrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.UpdateAccountingPaymenttermResponse](../../models/operations/updateaccountingpaymenttermresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |