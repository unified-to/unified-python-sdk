# Creditmemo

## Overview

### Available Operations

* [create_accounting_creditmemo](#create_accounting_creditmemo) - Create a creditmemo
* [get_accounting_creditmemo](#get_accounting_creditmemo) - Retrieve a creditmemo
* [list_accounting_creditmemoes](#list_accounting_creditmemoes) - List all creditmemoes
* [patch_accounting_creditmemo](#patch_accounting_creditmemo) - Update a creditmemo
* [remove_accounting_creditmemo](#remove_accounting_creditmemo) - Remove a creditmemo
* [update_accounting_creditmemo](#update_accounting_creditmemo) - Update a creditmemo

## create_accounting_creditmemo

Create a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingCreditmemo" method="post" path="/accounting/{connection_id}/creditmemo" example="accounting_creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.create_accounting_creditmemo(request={
        "accounting_creditmemo": {
            "applications": [],
            "attachments": [
                {
                    "download_url": "https://enlightened-chairperson.com/",
                    "id": "d9eb8b65-3bcd-40e0-9725-eb19bef2ea8e",
                    "mime_type": "complectus",
                    "name": "thesis",
                },
            ],
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "ulterius",
            "currency": "MKD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2023-10-18T04:35:00.543Z"),
            "id": "113e82c0-b1b0-4991-aca2-0ced743098f4",
            "lineitems": [],
            "metadata": [],
            "notes": "Dedecor amo adfero torqueo quas.",
            "payment_collection_method": shared.AccountingCreditmemoPaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "posted_at": parse_datetime("2025-11-16T03:08:24.670Z"),
            "refund_amount": 0.0,
            "refund_reason": "Virgo inflammatio quibusdam aestivus magnam.",
            "refunded_at": parse_datetime("2023-10-23T00:35:36.814Z"),
            "send": False,
            "status": shared.AccountingCreditmemoStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2024-11-15T22:10:42.464Z"),
            "url": "https://lighthearted-bandwidth.net/",
        },
        "connection_id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateAccountingCreditmemoRequest](../../models/operations/createaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreateAccountingCreditmemoResponse](../../models/operations/createaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_creditmemo

Retrieve a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingCreditmemo" method="get" path="/accounting/{connection_id}/creditmemo/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.get_accounting_creditmemo(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAccountingCreditmemoRequest](../../models/operations/getaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetAccountingCreditmemoResponse](../../models/operations/getaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_creditmemoes

List all creditmemoes

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingCreditmemoes" method="get" path="/accounting/{connection_id}/creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.list_accounting_creditmemoes(request={
        "connection_id": "<id>",
    })

    assert res.accounting_creditmemoes is not None

    # Handle response
    print(res.accounting_creditmemoes)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListAccountingCreditmemoesRequest](../../models/operations/listaccountingcreditmemoesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.ListAccountingCreditmemoesResponse](../../models/operations/listaccountingcreditmemoesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_creditmemo

Update a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingCreditmemo" method="patch" path="/accounting/{connection_id}/creditmemo/{id}" example="accounting_creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.patch_accounting_creditmemo(request={
        "accounting_creditmemo": {
            "applications": [],
            "attachments": [
                {
                    "download_url": "https://enlightened-chairperson.com/",
                    "id": "e55b0563-c907-4e07-9d69-be88719a30ce",
                    "mime_type": "complectus",
                    "name": "thesis",
                },
            ],
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "ulterius",
            "currency": "MKD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2023-10-18T04:35:00.543Z"),
            "id": "7f3f8929-231d-4f43-bbbc-558edfba2ebd",
            "lineitems": [],
            "metadata": [],
            "notes": "Dedecor amo adfero torqueo quas.",
            "payment_collection_method": shared.AccountingCreditmemoPaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "posted_at": parse_datetime("2025-11-16T03:08:24.704Z"),
            "refund_amount": 0.0,
            "refund_reason": "Virgo inflammatio quibusdam aestivus magnam.",
            "refunded_at": parse_datetime("2023-10-23T00:35:36.814Z"),
            "send": False,
            "status": shared.AccountingCreditmemoStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2024-11-15T22:10:42.482Z"),
            "url": "https://lighthearted-bandwidth.net/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchAccountingCreditmemoRequest](../../models/operations/patchaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.PatchAccountingCreditmemoResponse](../../models/operations/patchaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_creditmemo

Remove a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingCreditmemo" method="delete" path="/accounting/{connection_id}/creditmemo/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.remove_accounting_creditmemo(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.RemoveAccountingCreditmemoRequest](../../models/operations/removeaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.RemoveAccountingCreditmemoResponse](../../models/operations/removeaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_creditmemo

Update a creditmemo

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingCreditmemo" method="put" path="/accounting/{connection_id}/creditmemo/{id}" example="accounting_creditmemo" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.creditmemo.update_accounting_creditmemo(request={
        "accounting_creditmemo": {
            "applications": [],
            "attachments": [
                {
                    "download_url": "https://enlightened-chairperson.com/",
                    "id": "e55b0563-c907-4e07-9d69-be88719a30ce",
                    "mime_type": "complectus",
                    "name": "thesis",
                },
            ],
            "created_at": parse_datetime("2023-09-20T01:47:01.571Z"),
            "creditmemo_number": "ulterius",
            "currency": "MKD",
            "discount_amount": 0.0,
            "due_at": parse_datetime("2023-10-18T04:35:00.543Z"),
            "id": "7f3f8929-231d-4f43-bbbc-558edfba2ebd",
            "lineitems": [],
            "metadata": [],
            "notes": "Dedecor amo adfero torqueo quas.",
            "payment_collection_method": shared.AccountingCreditmemoPaymentCollectionMethod.CHARGE_AUTOMATICALLY,
            "posted_at": parse_datetime("2025-11-16T03:08:24.704Z"),
            "refund_amount": 0.0,
            "refund_reason": "Virgo inflammatio quibusdam aestivus magnam.",
            "refunded_at": parse_datetime("2023-10-23T00:35:36.814Z"),
            "send": False,
            "status": shared.AccountingCreditmemoStatus.PAID,
            "tax_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2024-11-15T22:10:42.482Z"),
            "url": "https://lighthearted-bandwidth.net/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_creditmemo is not None

    # Handle response
    print(res.accounting_creditmemo)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateAccountingCreditmemoRequest](../../models/operations/updateaccountingcreditmemorequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.UpdateAccountingCreditmemoResponse](../../models/operations/updateaccountingcreditmemoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |