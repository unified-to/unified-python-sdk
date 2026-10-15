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
            "approved_at": parse_datetime("2025-04-09T07:58:33.330Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "2e8c5dfd-e674-42c6-903a-8ccfa9352e17",
            "lineitems": [
                {
                    "id": "c3f3ddaa-c11f-4178-b209-84bee613e882",
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
                    "id": "fa018156-e8bc-44ce-8e5b-264cf5c92ebe",
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
            "posted_at": parse_datetime("2022-10-31T17:40:00.667Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-09T07:58:33.330Z"),
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
            "approved_at": parse_datetime("2025-04-09T07:58:33.368Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "72f103eb-1bde-416b-86a4-f73f022e67ff",
            "lineitems": [
                {
                    "id": "02ae146a-23a0-4a1f-9dfa-45cc1fc5bf83",
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
                    "id": "c58b4a98-f786-40b2-ade5-6fce51f3e00d",
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
            "posted_at": parse_datetime("2022-10-31T17:40:00.686Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-09T07:58:33.368Z"),
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
            "approved_at": parse_datetime("2025-04-09T07:58:33.368Z"),
            "attachments": [],
            "category_ids": [],
            "created_at": parse_datetime("2020-05-29T02:04:59.078Z"),
            "currency": "BMD",
            "external_number": "asporto",
            "id": "72f103eb-1bde-416b-86a4-f73f022e67ff",
            "lineitems": [
                {
                    "id": "02ae146a-23a0-4a1f-9dfa-45cc1fc5bf83",
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
                    "id": "c58b4a98-f786-40b2-ade5-6fce51f3e00d",
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
            "posted_at": parse_datetime("2022-10-31T17:40:00.686Z"),
            "reimbursed_amount": 6696.0,
            "status": shared.AccountingExpensereportStatus.PAID,
            "tax_amount": 983.0,
            "total_amount": 13931.0,
            "updated_at": parse_datetime("2025-04-09T07:58:33.368Z"),
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