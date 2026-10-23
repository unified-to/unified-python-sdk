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

Creates a AccountingExpensereport. Provide the unified AccountingExpensereport fields in the request body; they are mapped to the provider's API. Returns the created AccountingExpensereport.

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
            "approved_at": parse_datetime("2021-04-19T18:19:47.728Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "e7168e6f-5cc2-4a05-9baf-11284f81f286",
            "lineitems": [
                {
                    "id": "437c137d-bfd6-4fb7-8885-18496dd7eea4",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "a26e9f40-f44e-4a14-ade8-9c4fc374be2f",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "a21b5cbf-709a-4704-9e96-da1cccdc7c08",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "ec27d9f8-52eb-45fb-946c-059d7a4bbafa",
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
            "reimbursed_at": parse_datetime("2021-04-19T18:19:47.728Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T18:19:47.728Z"),
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

Retrieves a single AccountingExpensereport by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of AccountingExpensereports. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the AccountingExpensereport identified by `id`. Provide the unified AccountingExpensereport fields to change in the request body.

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
            "approved_at": parse_datetime("2021-04-19T18:19:47.732Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "f6d6b3ec-d74c-4395-a75c-8d47e3f19582",
            "lineitems": [
                {
                    "id": "8ed6f3f9-c59b-486e-9e66-e0a9aefe53fa",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "45dfacc4-9665-4c8c-8868-3e3a0613bda0",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "048afe4d-b46c-4391-944e-7804fffd869e",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "f51b37b0-a0f3-4cb9-a2f4-fef982cacd3b",
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
            "reimbursed_at": parse_datetime("2021-04-19T18:19:47.732Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T18:19:47.732Z"),
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

Deletes the AccountingExpensereport identified by `id`.

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

Updates the AccountingExpensereport identified by `id`. Provide the unified AccountingExpensereport fields to change in the request body.

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
            "approved_at": parse_datetime("2021-04-19T18:19:47.732Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "f6d6b3ec-d74c-4395-a75c-8d47e3f19582",
            "lineitems": [
                {
                    "id": "8ed6f3f9-c59b-486e-9e66-e0a9aefe53fa",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "45dfacc4-9665-4c8c-8868-3e3a0613bda0",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "048afe4d-b46c-4391-944e-7804fffd869e",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "f51b37b0-a0f3-4cb9-a2f4-fef982cacd3b",
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
            "reimbursed_at": parse_datetime("2021-04-19T18:19:47.732Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-19T18:19:47.732Z"),
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