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

Creates a AccountingInvoice. Provide the unified AccountingInvoice fields in the request body; they are mapped to the provider's API. Returns the created AccountingInvoice.

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
                    "id": "0e58b066-90a1-4a32-9610-6b8ec2791195",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "ca8dde87-5b7a-4aca-a722-833e68d8884a",
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
            "id": "2af86b01-ecfa-43e2-894d-c916aa32b136",
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
            "updated_at": parse_datetime("2026-04-27T22:44:07.478Z"),
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

Retrieves a single AccountingInvoice by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of AccountingInvoices. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the AccountingInvoice identified by `id`. Provide the unified AccountingInvoice fields to change in the request body.

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
                    "id": "23117704-3736-47fd-a25e-078272019187",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "eb040f33-7128-4cb2-9b2a-9ad55508cdfc",
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
            "id": "31c20839-77a9-4d37-abf8-813e725a2836",
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
            "updated_at": parse_datetime("2026-04-27T22:44:07.521Z"),
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

Deletes the AccountingInvoice identified by `id`.

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

Updates the AccountingInvoice identified by `id`. Provide the unified AccountingInvoice fields to change in the request body.

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
                    "id": "23117704-3736-47fd-a25e-078272019187",
                    "mime_type": "application/pdf",
                    "name": "INV-77705.pdf",
                },
                {
                    "download_url": "https://earnest-giggle.net",
                    "id": "eb040f33-7128-4cb2-9b2a-9ad55508cdfc",
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
            "id": "31c20839-77a9-4d37-abf8-813e725a2836",
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
            "updated_at": parse_datetime("2026-04-27T22:44:07.521Z"),
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