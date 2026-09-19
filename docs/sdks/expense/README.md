# Expense

## Overview

### Available Operations

* [create_accounting_expense](#create_accounting_expense) - Create an expense
* [get_accounting_expense](#get_accounting_expense) - Retrieve an expense
* [list_accounting_expenses](#list_accounting_expenses) - List all expenses
* [patch_accounting_expense](#patch_accounting_expense) - Update an expense
* [remove_accounting_expense](#remove_accounting_expense) - Remove an expense
* [update_accounting_expense](#update_accounting_expense) - Update an expense

## create_accounting_expense

Create an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingExpense" method="post" path="/accounting/{connection_id}/expense" example="accounting_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.create_accounting_expense(request={
        "accounting_expense": {
            "approved_at": parse_datetime("2026-05-10T15:28:02.446Z"),
            "attachments": [
                {
                    "download_url": "https://ripe-napkin.biz/",
                    "id": "2c89d9c9-f214-4a83-8a49-eb53567dda6e",
                    "mime_type": "annus",
                    "name": "cohibeo",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "SSP",
            "external_number": "necessitatibus",
            "id": "1a4584bd-095a-4b17-a464-9f2b4bc15f7c",
            "lineitems": [
                {
                    "id": "74fadc00-4e6f-4ef0-a00f-a7a1714a1e23",
                    "item_description": "Innovative Table featuring left technology and Rubber construction",
                    "item_name": "Luxurious Cotton Pizza",
                    "item_sku": "978-0-8324-6620-5",
                    "notes": "Degusto conventus defendo valetudo.",
                    "tax_amount": 2501.0,
                    "total_amount": 168.0,
                    "unit_amount": 3059.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Refined Steel Shoes",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2021-06-04T08:33:42.238Z"),
            "reimbursed_amount": 1833.0,
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 2602.0,
            "total_amount": 3580.0,
            "updated_at": parse_datetime("2026-05-10T15:28:02.446Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_expense is not None

    # Handle response
    print(res.accounting_expense)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingExpenseRequest](../../models/operations/createaccountingexpenserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingExpenseResponse](../../models/operations/createaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_expense

Retrieve an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingExpense" method="get" path="/accounting/{connection_id}/expense/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.get_accounting_expense(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expense is not None

    # Handle response
    print(res.accounting_expense)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingExpenseRequest](../../models/operations/getaccountingexpenserequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingExpenseResponse](../../models/operations/getaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_expenses

List all expenses

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingExpenses" method="get" path="/accounting/{connection_id}/expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.list_accounting_expenses(request={
        "connection_id": "<id>",
    })

    assert res.accounting_expenses is not None

    # Handle response
    print(res.accounting_expenses)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingExpensesRequest](../../models/operations/listaccountingexpensesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingExpensesResponse](../../models/operations/listaccountingexpensesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_expense

Update an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingExpense" method="patch" path="/accounting/{connection_id}/expense/{id}" example="accounting_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.patch_accounting_expense(request={
        "accounting_expense": {
            "approved_at": parse_datetime("2026-05-10T15:28:02.488Z"),
            "attachments": [
                {
                    "download_url": "https://ripe-napkin.biz/",
                    "id": "ce6fad02-03df-4bd9-bd53-03c3d01eabfa",
                    "mime_type": "annus",
                    "name": "cohibeo",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "SSP",
            "external_number": "necessitatibus",
            "id": "8a5cb950-617b-4246-bbfa-80448539cab4",
            "lineitems": [
                {
                    "id": "df246eca-f6fa-4131-997e-73e56dfaa3c3",
                    "item_description": "Innovative Table featuring left technology and Rubber construction",
                    "item_name": "Luxurious Cotton Pizza",
                    "item_sku": "978-0-8324-6620-5",
                    "notes": "Degusto conventus defendo valetudo.",
                    "tax_amount": 2501.0,
                    "total_amount": 168.0,
                    "unit_amount": 3059.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Refined Steel Shoes",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2021-06-04T08:33:42.245Z"),
            "reimbursed_amount": 1833.0,
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 2602.0,
            "total_amount": 3580.0,
            "updated_at": parse_datetime("2026-05-10T15:28:02.488Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expense is not None

    # Handle response
    print(res.accounting_expense)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingExpenseRequest](../../models/operations/patchaccountingexpenserequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingExpenseResponse](../../models/operations/patchaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_expense

Remove an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingExpense" method="delete" path="/accounting/{connection_id}/expense/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.remove_accounting_expense(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveAccountingExpenseRequest](../../models/operations/removeaccountingexpenserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingExpenseResponse](../../models/operations/removeaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_expense

Update an expense

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingExpense" method="put" path="/accounting/{connection_id}/expense/{id}" example="accounting_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.update_accounting_expense(request={
        "accounting_expense": {
            "approved_at": parse_datetime("2026-05-10T15:28:02.488Z"),
            "attachments": [
                {
                    "download_url": "https://ripe-napkin.biz/",
                    "id": "ce6fad02-03df-4bd9-bd53-03c3d01eabfa",
                    "mime_type": "annus",
                    "name": "cohibeo",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "SSP",
            "external_number": "necessitatibus",
            "id": "8a5cb950-617b-4246-bbfa-80448539cab4",
            "lineitems": [
                {
                    "id": "df246eca-f6fa-4131-997e-73e56dfaa3c3",
                    "item_description": "Innovative Table featuring left technology and Rubber construction",
                    "item_name": "Luxurious Cotton Pizza",
                    "item_sku": "978-0-8324-6620-5",
                    "notes": "Degusto conventus defendo valetudo.",
                    "tax_amount": 2501.0,
                    "total_amount": 168.0,
                    "unit_amount": 3059.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Refined Steel Shoes",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2021-06-04T08:33:42.245Z"),
            "reimbursed_amount": 1833.0,
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 2602.0,
            "total_amount": 3580.0,
            "updated_at": parse_datetime("2026-05-10T15:28:02.488Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_expense is not None

    # Handle response
    print(res.accounting_expense)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingExpenseRequest](../../models/operations/updateaccountingexpenserequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingExpenseResponse](../../models/operations/updateaccountingexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |