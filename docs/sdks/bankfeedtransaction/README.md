# Bankfeedtransaction

## Overview

### Available Operations

* [create_accounting_bankfeedtransaction](#create_accounting_bankfeedtransaction) - Create a bankfeedtransaction
* [get_accounting_bankfeedtransaction](#get_accounting_bankfeedtransaction) - Retrieve a bankfeedtransaction
* [list_accounting_bankfeedtransactions](#list_accounting_bankfeedtransactions) - List all bankfeedtransactions
* [patch_accounting_bankfeedtransaction](#patch_accounting_bankfeedtransaction) - Update a bankfeedtransaction
* [remove_accounting_bankfeedtransaction](#remove_accounting_bankfeedtransaction) - Remove a bankfeedtransaction
* [update_accounting_bankfeedtransaction](#update_accounting_bankfeedtransaction) - Update a bankfeedtransaction

## create_accounting_bankfeedtransaction

Create a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingBankfeedtransaction" method="post" path="/accounting/{connection_id}/bankfeedtransaction" example="accounting_bankfeedtransaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankfeedtransaction.create_accounting_bankfeedtransaction(request={
        "accounting_bankfeedtransaction": {
            "amount": 60889.0,
            "bank_category": "Clothing",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "CAD",
            "description": "Payment of SRD 92.72 for withdrawal at Halvorson - Ziemann, processed with card ending ****3731 linked to account ***7781.",
            "id": "9d7f1d1e-6836-421d-bcc7-0f960838a365",
            "is_pending": True,
            "merchant_name": "Buckridge - Feest",
            "metadata": [],
            "posted_at": parse_datetime("2025-04-14T19:54:37.886Z"),
            "reference": "79574105",
            "transaction_at": parse_datetime("2022-07-30T08:09:49.075Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-25T01:44:27.953Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_bankfeedtransaction is not None

    # Handle response
    print(res.accounting_bankfeedtransaction)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.CreateAccountingBankfeedtransactionRequest](../../models/operations/createaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.CreateAccountingBankfeedtransactionResponse](../../models/operations/createaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_bankfeedtransaction

Retrieve a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingBankfeedtransaction" method="get" path="/accounting/{connection_id}/bankfeedtransaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankfeedtransaction.get_accounting_bankfeedtransaction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedtransaction is not None

    # Handle response
    print(res.accounting_bankfeedtransaction)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetAccountingBankfeedtransactionRequest](../../models/operations/getaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.GetAccountingBankfeedtransactionResponse](../../models/operations/getaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_bankfeedtransactions

List all bankfeedtransactions

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingBankfeedtransactions" method="get" path="/accounting/{connection_id}/bankfeedtransaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankfeedtransaction.list_accounting_bankfeedtransactions(request={
        "connection_id": "<id>",
    })

    assert res.accounting_bankfeedtransactions is not None

    # Handle response
    print(res.accounting_bankfeedtransactions)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.ListAccountingBankfeedtransactionsRequest](../../models/operations/listaccountingbankfeedtransactionsrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.ListAccountingBankfeedtransactionsResponse](../../models/operations/listaccountingbankfeedtransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_bankfeedtransaction

Update a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingBankfeedtransaction" method="patch" path="/accounting/{connection_id}/bankfeedtransaction/{id}" example="accounting_bankfeedtransaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankfeedtransaction.patch_accounting_bankfeedtransaction(request={
        "accounting_bankfeedtransaction": {
            "amount": 60889.0,
            "bank_category": "Clothing",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "CAD",
            "description": "Payment of SRD 92.72 for withdrawal at Halvorson - Ziemann, processed with card ending ****3731 linked to account ***7781.",
            "id": "5b2d5916-e88b-4808-b28c-aa9646641043",
            "is_pending": True,
            "merchant_name": "Buckridge - Feest",
            "metadata": [],
            "posted_at": parse_datetime("2025-04-14T19:54:37.909Z"),
            "reference": "79574105",
            "transaction_at": parse_datetime("2022-07-30T08:09:49.077Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-25T01:44:27.954Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedtransaction is not None

    # Handle response
    print(res.accounting_bankfeedtransaction)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchAccountingBankfeedtransactionRequest](../../models/operations/patchaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.PatchAccountingBankfeedtransactionResponse](../../models/operations/patchaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_bankfeedtransaction

Remove a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingBankfeedtransaction" method="delete" path="/accounting/{connection_id}/bankfeedtransaction/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankfeedtransaction.remove_accounting_bankfeedtransaction(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.RemoveAccountingBankfeedtransactionRequest](../../models/operations/removeaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.RemoveAccountingBankfeedtransactionResponse](../../models/operations/removeaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_bankfeedtransaction

Update a bankfeedtransaction

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingBankfeedtransaction" method="put" path="/accounting/{connection_id}/bankfeedtransaction/{id}" example="accounting_bankfeedtransaction" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankfeedtransaction.update_accounting_bankfeedtransaction(request={
        "accounting_bankfeedtransaction": {
            "amount": 60889.0,
            "bank_category": "Clothing",
            "category_ids": [],
            "created_at": parse_datetime("2022-03-24T23:41:08.374Z"),
            "currency": "CAD",
            "description": "Payment of SRD 92.72 for withdrawal at Halvorson - Ziemann, processed with card ending ****3731 linked to account ***7781.",
            "id": "5b2d5916-e88b-4808-b28c-aa9646641043",
            "is_pending": True,
            "merchant_name": "Buckridge - Feest",
            "metadata": [],
            "posted_at": parse_datetime("2025-04-14T19:54:37.909Z"),
            "reference": "79574105",
            "transaction_at": parse_datetime("2022-07-30T08:09:49.077Z"),
            "type": shared.AccountingBankfeedtransactionType.CREDIT,
            "updated_at": parse_datetime("2022-05-25T01:44:27.954Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bankfeedtransaction is not None

    # Handle response
    print(res.accounting_bankfeedtransaction)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.UpdateAccountingBankfeedtransactionRequest](../../models/operations/updateaccountingbankfeedtransactionrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.UpdateAccountingBankfeedtransactionResponse](../../models/operations/updateaccountingbankfeedtransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |