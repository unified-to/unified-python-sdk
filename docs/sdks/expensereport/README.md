# Expensereport

## Overview

### Available Operations

* [create_accounting_expensereport](#create_accounting_expensereport) - Create an expensereport
* [get_accounting_expensereport](#get_accounting_expensereport) - Retrieve an expensereport
* [list_accounting_expensereports](#list_accounting_expensereports) - List all expensereports
* [patch_accounting_expensereport](#patch_accounting_expensereport) - Update an expensereport
* [remove_accounting_expensereport](#remove_accounting_expensereport) - Remove an expensereport
* [update_accounting_expensereport](#update_accounting_expensereport) - Update an expensereport

## create_accounting_expensereport

Create an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingExpensereport" method="post" path="/accounting/{connection_id}/expensereport" example="accounting_expensereport" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expensereport.create_accounting_expensereport(request={
        "accounting_expensereport": {
            "approved_at": parse_datetime("2021-04-19T11:28:31.620Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "0e1a2879-7c11-49b3-bf53-718d06608f52",
            "lineitems": [
                {
                    "id": "8953e182-2003-42db-bdd6-df7c41e5f07a",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "2872ca66-3046-4949-b93f-d4e7cf067339",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "774a00fb-0ad4-460b-b83a-74b274fc43e1",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "229b5e80-2e70-4671-8545-b4e23d6d4814",
                    "item_name": "Flight",
                    "tax_amount": 0.0,
                    "total_amount": 445.27,
                    "unit_amount": 445.27,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Lolita Kunde - October expenses",
            "posted_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "reimbursed_amount": 908.46,
            "reimbursed_at": parse_datetime("2021-04-19T11:28:31.620Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T11:28:31.620Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_expensereport is not None

    # Handle response
    print(res.accounting_expensereport)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateAccountingExpensereportRequest](../../models/operations/createaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.CreateAccountingExpensereportResponse](../../models/operations/createaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_expensereport

Retrieve an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingExpensereport" method="get" path="/accounting/{connection_id}/expensereport/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expensereport.get_accounting_expensereport(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expensereport is not None

    # Handle response
    print(res.accounting_expensereport)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAccountingExpensereportRequest](../../models/operations/getaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GetAccountingExpensereportResponse](../../models/operations/getaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_expensereports

List all expensereports

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingExpensereports" method="get" path="/accounting/{connection_id}/expensereport" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expensereport.list_accounting_expensereports(request={
        "connection_id": "<id>",
    })

    assert res.accounting_expensereports is not None

    # Handle response
    print(res.accounting_expensereports)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingExpensereportsRequest](../../models/operations/listaccountingexpensereportsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.ListAccountingExpensereportsResponse](../../models/operations/listaccountingexpensereportsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_expensereport

Update an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingExpensereport" method="patch" path="/accounting/{connection_id}/expensereport/{id}" example="accounting_expensereport" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expensereport.patch_accounting_expensereport(request={
        "accounting_expensereport": {
            "approved_at": parse_datetime("2021-04-19T11:28:31.627Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "2d99a3aa-894c-4130-9a8b-c6c1fea59f58",
            "lineitems": [
                {
                    "id": "47beed38-a624-45e4-897a-794497ae9250",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "45b133d0-943b-4580-9d37-96301611ed33",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "3abdb02e-5254-4d4f-91b3-e7915ea52258",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "44a7fd29-a498-434a-8bcb-c67bdb6e4632",
                    "item_name": "Flight",
                    "tax_amount": 0.0,
                    "total_amount": 445.27,
                    "unit_amount": 445.27,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Lolita Kunde - October expenses",
            "posted_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "reimbursed_amount": 908.46,
            "reimbursed_at": parse_datetime("2021-04-19T11:28:31.627Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T11:28:31.627Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expensereport is not None

    # Handle response
    print(res.accounting_expensereport)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchAccountingExpensereportRequest](../../models/operations/patchaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.PatchAccountingExpensereportResponse](../../models/operations/patchaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_expensereport

Remove an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingExpensereport" method="delete" path="/accounting/{connection_id}/expensereport/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expensereport.remove_accounting_expensereport(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.RemoveAccountingExpensereportRequest](../../models/operations/removeaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.RemoveAccountingExpensereportResponse](../../models/operations/removeaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_expensereport

Update an expensereport

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingExpensereport" method="put" path="/accounting/{connection_id}/expensereport/{id}" example="accounting_expensereport" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expensereport.update_accounting_expensereport(request={
        "accounting_expensereport": {
            "approved_at": parse_datetime("2021-04-19T11:28:31.627Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "2d99a3aa-894c-4130-9a8b-c6c1fea59f58",
            "lineitems": [
                {
                    "id": "47beed38-a624-45e4-897a-794497ae9250",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "45b133d0-943b-4580-9d37-96301611ed33",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "3abdb02e-5254-4d4f-91b3-e7915ea52258",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "44a7fd29-a498-434a-8bcb-c67bdb6e4632",
                    "item_name": "Flight",
                    "tax_amount": 0.0,
                    "total_amount": 445.27,
                    "unit_amount": 445.27,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Lolita Kunde - October expenses",
            "posted_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "reimbursed_amount": 908.46,
            "reimbursed_at": parse_datetime("2021-04-19T11:28:31.627Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T11:28:31.627Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expensereport is not None

    # Handle response
    print(res.accounting_expensereport)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateAccountingExpensereportRequest](../../models/operations/updateaccountingexpensereportrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.UpdateAccountingExpensereportResponse](../../models/operations/updateaccountingexpensereportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |