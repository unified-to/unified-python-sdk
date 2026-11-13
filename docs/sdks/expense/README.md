# Expense

## Overview

### Available Operations

* [create_accounting_expense](#create_accounting_expense) - Create an expense
* [create_legal_expense](#create_legal_expense) - Create an expense
* [get_accounting_expense](#get_accounting_expense) - Retrieve an expense
* [get_legal_expense](#get_legal_expense) - Retrieve an expense
* [list_accounting_expenses](#list_accounting_expenses) - List all expenses
* [list_legal_expenses](#list_legal_expenses) - List all expenses
* [patch_accounting_expense](#patch_accounting_expense) - Update an expense
* [patch_legal_expense](#patch_legal_expense) - Update an expense
* [remove_accounting_expense](#remove_accounting_expense) - Remove an expense
* [remove_legal_expense](#remove_legal_expense) - Remove an expense
* [update_accounting_expense](#update_accounting_expense) - Update an expense
* [update_legal_expense](#update_legal_expense) - Update an expense

## create_accounting_expense

Creates a AccountingExpense. Provide the unified AccountingExpense fields in the request body; they are mapped to the provider's API. Returns the created AccountingExpense.

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
            "attachments": [
                {
                    "download_url": "https://rubbery-couch.biz/",
                    "id": "b6ace541-5512-43d9-9986-e8638e153b0f",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://appropriate-smog.biz/",
                    "id": "ebcb4585-dd97-4093-b421-2b0ebe8f7b27",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "75cc4b90-782a-4916-a1a2-3e3550ae2cb2",
            "lineitems": [
                {
                    "id": "b67a40bd-7451-4979-8dc6-ac80df866940",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "1c65e7d0-f1b3-4692-8925-548d6a77856f",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "365c44e3-7534-4839-8279-6a12c64ed29a",
                    "item_name": "Conference ticket",
                    "notes": "Casus umquam conicio cinis demitto sint.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "bc863b53-2b56-4b00-8999-4ccb917fda5b",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "8c4a54c4-0f6c-463e-90c6-a7000f5491a0",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A payment of XPF 714.84 occurred at Bins, Barrows and Koch using a card ending in ****8422 for account ***4614.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-03T03:03:28.247Z"),
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

## create_legal_expense

Creates a LegalExpense. Provide the unified LegalExpense fields in the request body; they are mapped to the provider's API. Returns the created LegalExpense.

### Example Usage

<!-- UsageSnippet language="python" operationID="createLegalExpense" method="post" path="/legal/{connection_id}/expense" example="legal_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.create_legal_expense(request={
        "legal_expense": {
            "category": "Kids",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "MVR",
            "description": "Temporibus agnitio sui.",
            "id": "9022e9fc-78db-4d4e-b37b-64f38bc81853",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-04-13T02:15:38.311Z"),
        },
        "connection_id": "<id>",
    })

    assert res.legal_expense is not None

    # Handle response
    print(res.legal_expense)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateLegalExpenseRequest](../../models/operations/createlegalexpenserequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateLegalExpenseResponse](../../models/operations/createlegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_expense

Retrieves a single AccountingExpense by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

## get_legal_expense

Retrieves a single LegalExpense by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getLegalExpense" method="get" path="/legal/{connection_id}/expense/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.get_legal_expense(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_expense is not None

    # Handle response
    print(res.legal_expense)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetLegalExpenseRequest](../../models/operations/getlegalexpenserequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetLegalExpenseResponse](../../models/operations/getlegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_expenses

Returns a list of AccountingExpenses. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

## list_legal_expenses

Returns a list of LegalExpenses. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLegalExpenses" method="get" path="/legal/{connection_id}/expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.list_legal_expenses(request={
        "connection_id": "<id>",
    })

    assert res.legal_expenses is not None

    # Handle response
    print(res.legal_expenses)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListLegalExpensesRequest](../../models/operations/listlegalexpensesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListLegalExpensesResponse](../../models/operations/listlegalexpensesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_expense

Updates the AccountingExpense identified by `id`. Provide the unified AccountingExpense fields to change in the request body.

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
            "attachments": [
                {
                    "download_url": "https://rubbery-couch.biz/",
                    "id": "004169f6-a76c-4726-90f5-1ab07e39e40b",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://appropriate-smog.biz/",
                    "id": "c5f91c01-5aed-418e-951d-422d7a495c79",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "b9591d18-0b7c-4f92-9328-7fd47789ce7b",
            "lineitems": [
                {
                    "id": "d3ed64ee-d6f5-4802-bd00-5d8ccc3c7e84",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "cfd05836-1930-4377-82e9-112b3da720ff",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "91800d82-a970-4ce2-a26e-3a1dd84a7a93",
                    "item_name": "Conference ticket",
                    "notes": "Casus umquam conicio cinis demitto sint.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "3fd7a2f2-9884-441c-82ee-3b8c0f953060",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "cd972e04-f43b-4074-97c8-3deee14016e0",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A payment of XPF 714.84 occurred at Bins, Barrows and Koch using a card ending in ****8422 for account ***4614.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-03T03:03:28.249Z"),
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

## patch_legal_expense

Updates the LegalExpense identified by `id`. Provide the unified LegalExpense fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLegalExpense" method="patch" path="/legal/{connection_id}/expense/{id}" example="legal_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.patch_legal_expense(request={
        "legal_expense": {
            "category": "Kids",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "MVR",
            "description": "Temporibus agnitio sui.",
            "id": "48fed434-9aa9-4074-8bf0-1fa68d019861",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-04-13T02:15:38.320Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_expense is not None

    # Handle response
    print(res.legal_expense)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchLegalExpenseRequest](../../models/operations/patchlegalexpenserequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchLegalExpenseResponse](../../models/operations/patchlegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_expense

Deletes the AccountingExpense identified by `id`.

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

## remove_legal_expense

Deletes the LegalExpense identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLegalExpense" method="delete" path="/legal/{connection_id}/expense/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.remove_legal_expense(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveLegalExpenseRequest](../../models/operations/removelegalexpenserequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveLegalExpenseResponse](../../models/operations/removelegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_expense

Updates the AccountingExpense identified by `id`. Provide the unified AccountingExpense fields to change in the request body.

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
            "attachments": [
                {
                    "download_url": "https://rubbery-couch.biz/",
                    "id": "004169f6-a76c-4726-90f5-1ab07e39e40b",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://appropriate-smog.biz/",
                    "id": "c5f91c01-5aed-418e-951d-422d7a495c79",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "b9591d18-0b7c-4f92-9328-7fd47789ce7b",
            "lineitems": [
                {
                    "id": "d3ed64ee-d6f5-4802-bd00-5d8ccc3c7e84",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "cfd05836-1930-4377-82e9-112b3da720ff",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "91800d82-a970-4ce2-a26e-3a1dd84a7a93",
                    "item_name": "Conference ticket",
                    "notes": "Casus umquam conicio cinis demitto sint.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "3fd7a2f2-9884-441c-82ee-3b8c0f953060",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "cd972e04-f43b-4074-97c8-3deee14016e0",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A payment of XPF 714.84 occurred at Bins, Barrows and Koch using a card ending in ****8422 for account ***4614.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-03T03:03:28.249Z"),
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

## update_legal_expense

Updates the LegalExpense identified by `id`. Provide the unified LegalExpense fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLegalExpense" method="put" path="/legal/{connection_id}/expense/{id}" example="legal_expense" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.expense.update_legal_expense(request={
        "legal_expense": {
            "category": "Kids",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "MVR",
            "description": "Temporibus agnitio sui.",
            "id": "48fed434-9aa9-4074-8bf0-1fa68d019861",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-04-13T02:15:38.320Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.legal_expense is not None

    # Handle response
    print(res.legal_expense)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateLegalExpenseRequest](../../models/operations/updatelegalexpenserequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateLegalExpenseResponse](../../models/operations/updatelegalexpenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |