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
                    "id": "839c680a-29ed-48df-925c-e631524c0710",
                    "mime_type": "benevolentia",
                    "name": "vespillo",
                },
            ],
            "balance_amount": -1.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "RWF",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-11-27T21:25:37.363Z"),
            "extended_notes": [],
            "id": "758e134c-f0d1-4d34-819d-05e465afe423",
            "invoice_number": "vinco",
            "lineitems": [],
            "metadata": [],
            "notes": "Auctus comburo clarus ubi.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2022-11-25T15:00:28.871Z"),
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.SEND_INVOICE,
            "payments": [],
            "posted_at": parse_datetime("2026-03-27T18:21:59.653Z"),
            "reference": "adinventitias",
            "send": True,
            "status": shared.AccountingInvoiceStatus.DELETED,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_45,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.CREDITMEMO,
            "updated_at": parse_datetime("2023-02-06T08:15:01.501Z"),
            "url": "https://gifted-yarmulke.info/",
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
                    "id": "96161721-5d1f-44e1-9138-93227b7cc7e3",
                    "mime_type": "benevolentia",
                    "name": "vespillo",
                },
            ],
            "balance_amount": -1.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "RWF",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-11-27T21:25:37.363Z"),
            "extended_notes": [],
            "id": "0dbdc197-7b57-4bb3-9c3e-704abf27dfbd",
            "invoice_number": "vinco",
            "lineitems": [],
            "metadata": [],
            "notes": "Auctus comburo clarus ubi.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2022-11-25T15:00:28.871Z"),
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.SEND_INVOICE,
            "payments": [],
            "posted_at": parse_datetime("2026-03-27T18:21:59.699Z"),
            "reference": "adinventitias",
            "send": True,
            "status": shared.AccountingInvoiceStatus.DELETED,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_45,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.CREDITMEMO,
            "updated_at": parse_datetime("2023-02-06T08:15:01.504Z"),
            "url": "https://gifted-yarmulke.info/",
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
                    "id": "96161721-5d1f-44e1-9138-93227b7cc7e3",
                    "mime_type": "benevolentia",
                    "name": "vespillo",
                },
            ],
            "balance_amount": -1.0,
            "category_ids": [],
            "created_at": parse_datetime("2022-11-07T14:17:29.587Z"),
            "currency": "RWF",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2022-11-27T21:25:37.363Z"),
            "extended_notes": [],
            "id": "0dbdc197-7b57-4bb3-9c3e-704abf27dfbd",
            "invoice_number": "vinco",
            "lineitems": [],
            "metadata": [],
            "notes": "Auctus comburo clarus ubi.",
            "paid_amount": 0.0,
            "paid_at": parse_datetime("2022-11-25T15:00:28.871Z"),
            "payment_collection_method": shared.AccountingInvoicePaymentCollectionMethod.SEND_INVOICE,
            "payments": [],
            "posted_at": parse_datetime("2026-03-27T18:21:59.699Z"),
            "reference": "adinventitias",
            "send": True,
            "status": shared.AccountingInvoiceStatus.DELETED,
            "tax_amount": 0.0,
            "term": shared.AccountingInvoiceTerm.NET_45,
            "total_amount": 0.0,
            "type": shared.AccountingInvoiceType.CREDITMEMO,
            "updated_at": parse_datetime("2023-02-06T08:15:01.504Z"),
            "url": "https://gifted-yarmulke.info/",
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