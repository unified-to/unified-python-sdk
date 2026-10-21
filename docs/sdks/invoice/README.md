# Invoice

## Overview

### Available Operations

* [create_accounting_invoice](#create_accounting_invoice) - Create an invoice
* [get_accounting_invoice](#get_accounting_invoice) - Retrieve an invoice
* [list_accounting_invoices](#list_accounting_invoices) - List all invoices
* [patch_accounting_invoice](#patch_accounting_invoice) - Update an invoice
* [remove_accounting_invoice](#remove_accounting_invoice) - Remove an invoice
* [update_accounting_invoice](#update_accounting_invoice) - Update an invoice

## create_accounting_invoice

Create an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingInvoice" method="post" path="/accounting/{connection_id}/invoice" example="accounting_invoice" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.invoice.create_accounting_invoice(request={
        "accounting_invoice": {
            "attachments": [
                {
                    "download_url": "https://glossy-markup.net/",
                    "id": "998ae156-c453-4d71-abbb-89e52529ec22",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "0129f312-930f-4108-b08e-f4656be84d9d",
                    "mime_type": "application/pdf",
                    "name": "INV-77705-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "GBP",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-12-07T14:17:29.587Z"),
            "extended_notes": [],
            "id": "fafb36d3-1c5b-4d6a-86e8-647876ceed5b",
            "invoice_number": "INV-77705",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "metadata": [],
            "notes": "Adinventitias sursum temptatio auctus comburo clarus ubi deprimo.",
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "reference": "PO-2331",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.OVERDUE,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_25,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.INVOICE,
            "updated_at": parse_datetime("2026-04-23T12:59:16.962Z"),
            "url": "https://gifted-yarmulke.info/invoices/INV-77705",
        },
        "connection_id": "<id>",
    })

    assert res.accounting_invoice is not None

    # Handle response
    print(res.accounting_invoice)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateAccountingInvoiceRequest](../../models/operations/createaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateAccountingInvoiceResponse](../../models/operations/createaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_invoice

Retrieve an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingInvoice" method="get" path="/accounting/{connection_id}/invoice/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.invoice.get_accounting_invoice(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_invoice is not None

    # Handle response
    print(res.accounting_invoice)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingInvoiceRequest](../../models/operations/getaccountinginvoicerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetAccountingInvoiceResponse](../../models/operations/getaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_invoices

List all invoices

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingInvoices" method="get" path="/accounting/{connection_id}/invoice" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.invoice.list_accounting_invoices(request={
        "connection_id": "<id>",
    })

    assert res.accounting_invoices is not None

    # Handle response
    print(res.accounting_invoices)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingInvoicesRequest](../../models/operations/listaccountinginvoicesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListAccountingInvoicesResponse](../../models/operations/listaccountinginvoicesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_invoice

Update an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingInvoice" method="patch" path="/accounting/{connection_id}/invoice/{id}" example="accounting_invoice" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.invoice.patch_accounting_invoice(request={
        "accounting_invoice": {
            "attachments": [
                {
                    "download_url": "https://glossy-markup.net/",
                    "id": "f53b24c3-e4b4-4b63-9ca3-a217cf37ed77",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "8b7e8a9d-a64c-40a7-8e73-015681e8d6b3",
                    "mime_type": "application/pdf",
                    "name": "INV-77705-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "GBP",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-12-07T14:17:29.587Z"),
            "extended_notes": [],
            "id": "723b6a86-69df-4120-b5f1-f0aa4ee07386",
            "invoice_number": "INV-77705",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "metadata": [],
            "notes": "Adinventitias sursum temptatio auctus comburo clarus ubi deprimo.",
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "reference": "PO-2331",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.OVERDUE,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_25,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.INVOICE,
            "updated_at": parse_datetime("2026-04-23T12:59:17.076Z"),
            "url": "https://gifted-yarmulke.info/invoices/INV-77705",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_invoice is not None

    # Handle response
    print(res.accounting_invoice)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchAccountingInvoiceRequest](../../models/operations/patchaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchAccountingInvoiceResponse](../../models/operations/patchaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_invoice

Remove an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingInvoice" method="delete" path="/accounting/{connection_id}/invoice/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.invoice.remove_accounting_invoice(request={
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
| `request`                                                                                              | [operations.RemoveAccountingInvoiceRequest](../../models/operations/removeaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveAccountingInvoiceResponse](../../models/operations/removeaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_invoice

Update an invoice

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingInvoice" method="put" path="/accounting/{connection_id}/invoice/{id}" example="accounting_invoice" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.invoice.update_accounting_invoice(request={
        "accounting_invoice": {
            "attachments": [
                {
                    "download_url": "https://glossy-markup.net/",
                    "id": "f53b24c3-e4b4-4b63-9ca3-a217cf37ed77",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "8b7e8a9d-a64c-40a7-8e73-015681e8d6b3",
                    "mime_type": "application/pdf",
                    "name": "INV-77705-1.pdf",
                },
            ],
            "balance_amount": 0.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "GBP",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-12-07T14:17:29.587Z"),
            "extended_notes": [],
            "id": "723b6a86-69df-4120-b5f1-f0aa4ee07386",
            "invoice_number": "INV-77705",
            "is_inclusive_of_tax": False,
            "lineitems": [],
            "metadata": [],
            "notes": "Adinventitias sursum temptatio auctus comburo clarus ubi deprimo.",
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "payments": [],
            "posted_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "reference": "PO-2331",
            "salesorder_ids": [],
            "send": True,
            "status": shared.AccountingInvoiceStatus.OVERDUE,
            "sub_total_amount": 0.0,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_25,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.INVOICE,
            "updated_at": parse_datetime("2026-04-23T12:59:17.076Z"),
            "url": "https://gifted-yarmulke.info/invoices/INV-77705",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_invoice is not None

    # Handle response
    print(res.accounting_invoice)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateAccountingInvoiceRequest](../../models/operations/updateaccountinginvoicerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateAccountingInvoiceResponse](../../models/operations/updateaccountinginvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |