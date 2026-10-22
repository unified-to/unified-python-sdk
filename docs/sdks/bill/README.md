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

Creates a AccountingBill. Provide the unified AccountingBill fields in the request body; they are mapped to the provider's API. Returns the created AccountingBill.

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
            "attachments": [
                {
                    "download_url": "https://puny-foodstuffs.name",
                    "id": "6c9209f9-761e-4b05-bad7-d11aada20346",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466.pdf",
                },
                {
                    "download_url": "https://grimy-characterization.net",
                    "id": "043c0df2-d8b5-4766-856e-78913fedeec5",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "bill_number": "BILL-2466",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-09-07T23:03:14.104Z"),
            "extended_notes": [],
            "id": "b0d3a065-8e95-4707-848a-38944e7d7452",
            "lineitems": [],
            "metadata": [],
            "notes": "Admiratio deporto tutamen cilicium infit amissio ante demulceo.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2019-08-15T17:24:28.313Z"),
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.PARTIALLY_PAID,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_90,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2020-06-01T08:26:07.744Z"),
            "url": "https://cluttered-importance.org/bills/BILL-2466",
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

Retrieves a single AccountingBill by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of AccountingBills. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the AccountingBill identified by `id`. Provide the unified AccountingBill fields to change in the request body.

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
            "attachments": [
                {
                    "download_url": "https://puny-foodstuffs.name",
                    "id": "4527ae4f-25b4-4131-a05b-228a6f649e97",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466.pdf",
                },
                {
                    "download_url": "https://grimy-characterization.net",
                    "id": "5743dca5-30a1-4e95-92ce-8a27d46e5b0c",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "bill_number": "BILL-2466",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-09-07T23:03:14.104Z"),
            "extended_notes": [],
            "id": "ebe23029-ea98-4dc0-a1ec-eb5de14a04e5",
            "lineitems": [],
            "metadata": [],
            "notes": "Admiratio deporto tutamen cilicium infit amissio ante demulceo.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2019-08-15T17:24:28.313Z"),
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.PARTIALLY_PAID,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_90,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2020-06-01T08:26:07.748Z"),
            "url": "https://cluttered-importance.org/bills/BILL-2466",
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

Deletes the AccountingBill identified by `id`.

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

Updates the AccountingBill identified by `id`. Provide the unified AccountingBill fields to change in the request body.

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
            "attachments": [
                {
                    "download_url": "https://puny-foodstuffs.name",
                    "id": "4527ae4f-25b4-4131-a05b-228a6f649e97",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466.pdf",
                },
                {
                    "download_url": "https://grimy-characterization.net",
                    "id": "5743dca5-30a1-4e95-92ce-8a27d46e5b0c",
                    "mime_type": "application/pdf",
                    "name": "BILL-2466-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "bill_number": "BILL-2466",
            "category_ids": [],
            "created_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2019-09-07T23:03:14.104Z"),
            "extended_notes": [],
            "id": "ebe23029-ea98-4dc0-a1ec-eb5de14a04e5",
            "lineitems": [],
            "metadata": [],
            "notes": "Admiratio deporto tutamen cilicium infit amissio ante demulceo.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2019-08-15T17:24:28.313Z"),
            "payment_collection_method": shared.PaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2019-08-08T23:03:14.104Z"),
            "purchaseorder_ids": [],
            "send": True,
            "status": shared.AccountingBillStatus.PARTIALLY_PAID,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.Term.NET_90,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2020-06-01T08:26:07.748Z"),
            "url": "https://cluttered-importance.org/bills/BILL-2466",
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