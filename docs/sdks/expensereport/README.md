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
            "approved_at": parse_datetime("2025-04-10T02:50:34.449Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "f9633028-3e64-463f-a518-19c87fb925ec",
            "lineitems": [
                {
                    "id": "08a4c1d0-8742-4954-81ed-3d09136eac4e",
                    "item_description": "The Synchronised motivating software Car offers reliable performance and webbed design",
                    "item_name": "Intelligent Gold Cheese",
                    "item_sku": "978-0-6550-0228-4",
                    "notes": "Utrimque quas vesica spes.",
                    "tax_amount": 448.0,
                    "total_amount": 10875.0,
                    "unit_amount": 4092.0,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "0c9366c8-e1c5-4c5e-b34e-1deba5ae6001",
                    "item_description": "Ergonomic Bike made with Marble for all-day coordinated support",
                    "item_name": "Practical Steel Pizza",
                    "item_sku": "978-1-4129-9332-6",
                    "notes": "Corrumpo.",
                    "tax_amount": 875.0,
                    "total_amount": 12363.0,
                    "unit_amount": 6783.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Rustic Aluminum Car",
            "posted_at": parse_datetime("2022-11-01T03:04:26.646Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-10T02:50:34.449Z"),
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
            "approved_at": parse_datetime("2025-04-10T02:50:34.469Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "08f414b1-625d-4125-9615-2b09a8a33411",
            "lineitems": [
                {
                    "id": "bd731da1-ce69-4503-bc61-6b894fe0cc68",
                    "item_description": "The Synchronised motivating software Car offers reliable performance and webbed design",
                    "item_name": "Intelligent Gold Cheese",
                    "item_sku": "978-0-6550-0228-4",
                    "notes": "Utrimque quas vesica spes.",
                    "tax_amount": 448.0,
                    "total_amount": 10875.0,
                    "unit_amount": 4092.0,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "ee7f9f7b-bf7e-49e3-b578-b878abb0e2d0",
                    "item_description": "Ergonomic Bike made with Marble for all-day coordinated support",
                    "item_name": "Practical Steel Pizza",
                    "item_sku": "978-1-4129-9332-6",
                    "notes": "Corrumpo.",
                    "tax_amount": 875.0,
                    "total_amount": 12363.0,
                    "unit_amount": 6783.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Rustic Aluminum Car",
            "posted_at": parse_datetime("2022-11-01T03:04:26.656Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-10T02:50:34.469Z"),
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
            "approved_at": parse_datetime("2025-04-10T02:50:34.469Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "08f414b1-625d-4125-9615-2b09a8a33411",
            "lineitems": [
                {
                    "id": "bd731da1-ce69-4503-bc61-6b894fe0cc68",
                    "item_description": "The Synchronised motivating software Car offers reliable performance and webbed design",
                    "item_name": "Intelligent Gold Cheese",
                    "item_sku": "978-0-6550-0228-4",
                    "notes": "Utrimque quas vesica spes.",
                    "tax_amount": 448.0,
                    "total_amount": 10875.0,
                    "unit_amount": 4092.0,
                    "unit_quantity": 1.0,
                },
                {
                    "id": "ee7f9f7b-bf7e-49e3-b578-b878abb0e2d0",
                    "item_description": "Ergonomic Bike made with Marble for all-day coordinated support",
                    "item_name": "Practical Steel Pizza",
                    "item_sku": "978-1-4129-9332-6",
                    "notes": "Corrumpo.",
                    "tax_amount": 875.0,
                    "total_amount": 12363.0,
                    "unit_amount": 6783.0,
                    "unit_quantity": 1.0,
                },
            ],
            "metadata": [],
            "name": "Rustic Aluminum Car",
            "posted_at": parse_datetime("2022-11-01T03:04:26.656Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-10T02:50:34.469Z"),
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