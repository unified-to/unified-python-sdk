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
            "approved_at": parse_datetime("2021-04-21T06:52:44.963Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "b5c95101-ea78-461e-9c55-20fcf641ca47",
            "lineitems": [
                {
                    "id": "9a1c7605-e38f-43a1-a5e3-3ffbc73d5b78",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "7eae46d6-3d92-49bd-a061-a57105c875a3",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "c50468c0-3d72-4a0f-a9df-0bfa22545bc4",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "459437e0-0163-4ac9-96b0-dceeff7cc66f",
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
            "reimbursed_at": parse_datetime("2021-04-21T06:52:44.963Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-21T06:52:44.963Z"),
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
            "approved_at": parse_datetime("2021-04-21T06:52:44.968Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "213785df-5181-46f3-8485-ee5969de0157",
            "lineitems": [
                {
                    "id": "05d8ad88-80ce-4fd7-83a2-138118cb6e95",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "531af740-624a-4e96-b7ad-10fff85001cc",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "3b97fed2-27f1-47a0-8c4a-f62c56c82851",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "4f05e67e-8ab5-4da7-9268-f3bad1e3270d",
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
            "reimbursed_at": parse_datetime("2021-04-21T06:52:44.968Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-21T06:52:44.968Z"),
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
            "approved_at": parse_datetime("2021-04-21T06:52:44.968Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "GBP",
            "external_number": "ER-31240",
            "id": "213785df-5181-46f3-8485-ee5969de0157",
            "lineitems": [
                {
                    "id": "05d8ad88-80ce-4fd7-83a2-138118cb6e95",
                    "item_name": "Conference ticket",
                    "tax_amount": 0.0,
                    "total_amount": 39.9,
                    "unit_amount": 39.9,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "531af740-624a-4e96-b7ad-10fff85001cc",
                    "item_name": "Flight",
                    "notes": "Soluta omnis dolor.",
                    "tax_amount": 0.0,
                    "total_amount": 193.17,
                    "unit_amount": 193.17,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "3b97fed2-27f1-47a0-8c4a-f62c56c82851",
                    "item_name": "Client dinner",
                    "notes": "Altus caveo capio.",
                    "tax_amount": 0.0,
                    "total_amount": 230.12,
                    "unit_amount": 230.12,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "4f05e67e-8ab5-4da7-9268-f3bad1e3270d",
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
            "reimbursed_at": parse_datetime("2021-04-21T06:52:44.968Z"),
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 908.46,
            "updated_at": parse_datetime("2021-04-21T06:52:44.968Z"),
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