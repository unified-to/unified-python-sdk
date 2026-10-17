# Bill

## Overview

### Available Operations

* [create_accounting_bill](#create_accounting_bill) - Create a bill
* [get_accounting_bill](#get_accounting_bill) - Retrieve a bill
* [list_accounting_bills](#list_accounting_bills) - List all bills
* [patch_accounting_bill](#patch_accounting_bill) - Update a bill
* [remove_accounting_bill](#remove_accounting_bill) - Remove a bill
* [update_accounting_bill](#update_accounting_bill) - Update a bill

## create_accounting_bill

Create a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingBill" method="post" path="/accounting/{connection_id}/bill" example="accounting_bill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bill.create_accounting_bill(request={
        "accounting_bill": {
            "attachments": [],
            "bill_number": "vitae",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "AUD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-08-11T20:52:55.321Z"),
            "extended_notes": [],
            "id": "aeea768a-c0a4-4160-900b-7968cafca2d4",
            "lineitems": [],
            "metadata": [],
            "notes": "Tutamen cilicium infit.",
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2024-04-23T07:07:29.805Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_10,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-02-20T09:02:13.289Z"),
            "url": "https://coarse-interviewer.biz/",
        },
        "connection_id": "<id>",
    })

    assert res.accounting_bill is not None

    # Handle response
    print(res.accounting_bill)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateAccountingBillRequest](../../models/operations/createaccountingbillrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateAccountingBillResponse](../../models/operations/createaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_bill

Retrieve a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingBill" method="get" path="/accounting/{connection_id}/bill/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bill.get_accounting_bill(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bill is not None

    # Handle response
    print(res.accounting_bill)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAccountingBillRequest](../../models/operations/getaccountingbillrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GetAccountingBillResponse](../../models/operations/getaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_bills

List all bills

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingBills" method="get" path="/accounting/{connection_id}/bill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bill.list_accounting_bills(request={
        "connection_id": "<id>",
    })

    assert res.accounting_bills is not None

    # Handle response
    print(res.accounting_bills)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListAccountingBillsRequest](../../models/operations/listaccountingbillsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.ListAccountingBillsResponse](../../models/operations/listaccountingbillsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_bill

Update a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingBill" method="patch" path="/accounting/{connection_id}/bill/{id}" example="accounting_bill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bill.patch_accounting_bill(request={
        "accounting_bill": {
            "attachments": [],
            "bill_number": "vitae",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "AUD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-08-11T20:52:55.321Z"),
            "extended_notes": [],
            "id": "11259d06-f465-4753-aa28-687abaa42b83",
            "lineitems": [],
            "metadata": [],
            "notes": "Tutamen cilicium infit.",
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2024-04-23T07:07:29.827Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_10,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-02-20T09:02:13.315Z"),
            "url": "https://coarse-interviewer.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bill is not None

    # Handle response
    print(res.accounting_bill)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchAccountingBillRequest](../../models/operations/patchaccountingbillrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PatchAccountingBillResponse](../../models/operations/patchaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_bill

Remove a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingBill" method="delete" path="/accounting/{connection_id}/bill/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bill.remove_accounting_bill(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveAccountingBillRequest](../../models/operations/removeaccountingbillrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.RemoveAccountingBillResponse](../../models/operations/removeaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_bill

Update a bill

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingBill" method="put" path="/accounting/{connection_id}/bill/{id}" example="accounting_bill" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bill.update_accounting_bill(request={
        "accounting_bill": {
            "attachments": [],
            "bill_number": "vitae",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "AUD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-08-11T20:52:55.321Z"),
            "extended_notes": [],
            "id": "11259d06-f465-4753-aa28-687abaa42b83",
            "lineitems": [],
            "metadata": [],
            "notes": "Tutamen cilicium infit.",
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2024-04-23T07:07:29.827Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.DELETED,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_10,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2025-02-20T09:02:13.315Z"),
            "url": "https://coarse-interviewer.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_bill is not None

    # Handle response
    print(res.accounting_bill)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateAccountingBillRequest](../../models/operations/updateaccountingbillrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UpdateAccountingBillResponse](../../models/operations/updateaccountingbillresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |