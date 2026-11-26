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
                    "download_url": "https://avaricious-larva.biz",
                    "id": "f8141f3a-0e52-4de1-9dde-b8460b2fb1a6",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://precious-comparison.net/",
                    "id": "8c51bc71-9ba2-49c7-877e-9303778a40d2",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "fa5df863-b3fc-4b8d-a009-cf395602f8f3",
            "lineitems": [
                {
                    "id": "0ac7f165-780a-419d-9caa-822afd83bc04",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "992c7a5d-0f45-435f-852e-c6257ee49870",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "098da77a-0919-473c-a063-586411a52d06",
                    "item_name": "Conference ticket",
                    "notes": "Sint spiculum carcer ago charisma.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "78fbc5b1-9153-4630-9a26-8e08c033abc6",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "1a63199c-3e62-4559-8c00-dbf3d2889cd3",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A deposit for KPW 867.85 was made at Kohler LLC via card ending ****1416 on account ***1040.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-03T14:10:13.306Z"),
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
            "category": "Baby",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "GBP",
            "description": "Nihil sono villa voluptate cohibeo quas volo succurro.",
            "id": "3f981a2f-2a1b-443a-bcad-734b4b605a1a",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-04-20T11:15:23.658Z"),
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
                    "download_url": "https://avaricious-larva.biz",
                    "id": "067a3bd8-18f0-496f-9a59-79dddde95791",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://precious-comparison.net/",
                    "id": "533dca54-cd52-4954-8c89-51124fbb2e23",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "8c83a8de-1415-422b-8205-bb8b12ffed5e",
            "lineitems": [
                {
                    "id": "0d2d1961-5880-472e-9d2b-30c9cb823283",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "9e01d4e6-b05a-40e0-9685-688d0d02d289",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "55f7e715-00be-40f2-b35b-eb924ef23f08",
                    "item_name": "Conference ticket",
                    "notes": "Sint spiculum carcer ago charisma.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "a5fa92d2-7aee-4af3-b220-c7c437c7d631",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "c6a6fd37-746a-4dab-abc3-e04ccb3e1fc1",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A deposit for KPW 867.85 was made at Kohler LLC via card ending ****1416 on account ***1040.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-03T14:10:13.308Z"),
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
            "category": "Baby",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "GBP",
            "description": "Nihil sono villa voluptate cohibeo quas volo succurro.",
            "id": "fadf78d6-db44-4db1-b9ed-c24916f6ac77",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-04-20T11:15:23.666Z"),
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
                    "download_url": "https://avaricious-larva.biz",
                    "id": "067a3bd8-18f0-496f-9a59-79dddde95791",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696.pdf",
                },
                {
                    "download_url": "https://precious-comparison.net/",
                    "id": "533dca54-cd52-4954-8c89-51124fbb2e23",
                    "mime_type": "application/pdf",
                    "name": "receipt-9696-1.pdf",
                },
            ],
            "category_ids": [],
            "created_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "currency": "GBP",
            "external_number": "EXP-38303",
            "id": "8c83a8de-1415-422b-8205-bb8b12ffed5e",
            "lineitems": [
                {
                    "id": "0d2d1961-5880-472e-9d2b-30c9cb823283",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 364.74,
                    "unit_amount": 364.74,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "9e01d4e6-b05a-40e0-9685-688d0d02d289",
                    "item_name": "Client dinner",
                    "tax_amount": 0.0,
                    "total_amount": 258.35,
                    "unit_amount": 258.35,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "55f7e715-00be-40f2-b35b-eb924ef23f08",
                    "item_name": "Conference ticket",
                    "notes": "Sint spiculum carcer ago charisma.",
                    "tax_amount": 0.0,
                    "total_amount": 28.14,
                    "unit_amount": 28.14,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "a5fa92d2-7aee-4af3-b220-c7c437c7d631",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 157.04,
                    "unit_amount": 157.04,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "c6a6fd37-746a-4dab-abc3-e04ccb3e1fc1",
                    "item_name": "Hotel",
                    "tax_amount": 0.0,
                    "total_amount": 164.02,
                    "unit_amount": 164.02,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "A deposit for KPW 867.85 was made at Kohler LLC via card ending ****1416 on account ***1040.",
            "payment_method": "CASH",
            "posted_at": parse_datetime("2020-06-11T03:39:37.305Z"),
            "status": shared.AccountingExpenseStatus.SUBMITTED,
            "tax_amount": 0.0,
            "total_amount": 972.29,
            "type": shared.AccountingExpenseType.COMPANY,
            "updated_at": parse_datetime("2020-09-03T14:10:13.308Z"),
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
            "category": "Baby",
            "created_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "currency": "GBP",
            "description": "Nihil sono villa voluptate cohibeo quas volo succurro.",
            "id": "fadf78d6-db44-4db1-b9ed-c24916f6ac77",
            "incurred_at": parse_datetime("2020-11-08T00:41:42.356Z"),
            "is_billed": False,
            "metadata": [],
            "price_amount": 100.0,
            "quantity": 3.0,
            "total_amount": 300.0,
            "type": shared.LegalExpenseType.OTHER,
            "updated_at": parse_datetime("2024-04-20T11:15:23.666Z"),
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