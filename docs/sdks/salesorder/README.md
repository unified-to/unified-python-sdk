# Salesorder

## Overview

### Available Operations

* [create_accounting_salesorder](#create_accounting_salesorder) - Create a salesorder
* [get_accounting_salesorder](#get_accounting_salesorder) - Retrieve a salesorder
* [list_accounting_salesorders](#list_accounting_salesorders) - List all salesorders
* [patch_accounting_salesorder](#patch_accounting_salesorder) - Update a salesorder
* [remove_accounting_salesorder](#remove_accounting_salesorder) - Remove a salesorder
* [update_accounting_salesorder](#update_accounting_salesorder) - Update a salesorder

## create_accounting_salesorder

Creates a AccountingSalesorder. Provide the unified AccountingSalesorder fields in the request body; they are mapped to the provider's API. Returns the created AccountingSalesorder.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingSalesorder" method="post" path="/accounting/{connection_id}/salesorder" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.create_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-03-25T18:51:55.584Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "fees": [],
            "fulfillment_type": shared.FulfillmentType.OTHER,
            "id": "31b40f4c-8c74-473c-834c-108a496eb083",
            "lineitems": [],
            "metadata": [],
            "order_number": "832663",
            "payments": [],
            "posted_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Wholesale",
            "service_charge_amount": 0.0,
            "shipping_address": {
                "address1": "69878 Bradley Mill",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.PAID,
            "subtotal_amount": 0.0,
            "tax_amount": 0.0,
            "tip_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-03-25T18:51:55.584Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateAccountingSalesorderRequest](../../models/operations/createaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreateAccountingSalesorderResponse](../../models/operations/createaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_salesorder

Retrieves a single AccountingSalesorder by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingSalesorder" method="get" path="/accounting/{connection_id}/salesorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.get_accounting_salesorder(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAccountingSalesorderRequest](../../models/operations/getaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetAccountingSalesorderResponse](../../models/operations/getaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_salesorders

Returns a list of AccountingSalesorders. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingSalesorders" method="get" path="/accounting/{connection_id}/salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.list_accounting_salesorders(request={
        "connection_id": "<id>",
    })

    assert res.accounting_salesorders is not None

    # Handle response
    print(res.accounting_salesorders)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListAccountingSalesordersRequest](../../models/operations/listaccountingsalesordersrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListAccountingSalesordersResponse](../../models/operations/listaccountingsalesordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_salesorder

Updates the AccountingSalesorder identified by `id`. Provide the unified AccountingSalesorder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingSalesorder" method="patch" path="/accounting/{connection_id}/salesorder/{id}" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.patch_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-03-25T18:51:55.597Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "fees": [],
            "fulfillment_type": shared.FulfillmentType.OTHER,
            "id": "eb857dee-e60e-475f-bdcd-edb5a376f942",
            "lineitems": [],
            "metadata": [],
            "order_number": "832663",
            "payments": [],
            "posted_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Wholesale",
            "service_charge_amount": 0.0,
            "shipping_address": {
                "address1": "69878 Bradley Mill",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.PAID,
            "subtotal_amount": 0.0,
            "tax_amount": 0.0,
            "tip_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-03-25T18:51:55.597Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchAccountingSalesorderRequest](../../models/operations/patchaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.PatchAccountingSalesorderResponse](../../models/operations/patchaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_salesorder

Deletes the AccountingSalesorder identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingSalesorder" method="delete" path="/accounting/{connection_id}/salesorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.remove_accounting_salesorder(request={
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
| `request`                                                                                                    | [operations.RemoveAccountingSalesorderRequest](../../models/operations/removeaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.RemoveAccountingSalesorderResponse](../../models/operations/removeaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_salesorder

Updates the AccountingSalesorder identified by `id`. Provide the unified AccountingSalesorder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingSalesorder" method="put" path="/accounting/{connection_id}/salesorder/{id}" example="accounting_salesorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.salesorder.update_accounting_salesorder(request={
        "accounting_salesorder": {
            "billing_address": {
                "address1": "26530 Stroman Rest",
                "address2": "Suite 801",
                "city": "Pocatello",
                "country_code": "US",
                "postal_code": "05015-8546",
                "region": "Louisiana",
                "region_code": "MO",
            },
            "category_ids": [],
            "closed_at": parse_datetime("2023-03-25T18:51:55.597Z"),
            "created_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "fees": [],
            "fulfillment_type": shared.FulfillmentType.OTHER,
            "id": "eb857dee-e60e-475f-bdcd-edb5a376f942",
            "lineitems": [],
            "metadata": [],
            "order_number": "832663",
            "payments": [],
            "posted_at": parse_datetime("2022-01-17T16:11:50.310Z"),
            "refunded_amount": 0.0,
            "sales_channel": "Wholesale",
            "service_charge_amount": 0.0,
            "shipping_address": {
                "address1": "69878 Bradley Mill",
                "city": "Port Matildestad",
                "country_code": "US",
                "postal_code": "07989-2148",
                "region": "Arkansas",
                "region_code": "AK",
            },
            "status": shared.AccountingSalesorderStatus.PAID,
            "subtotal_amount": 0.0,
            "tax_amount": 0.0,
            "tip_amount": 0.0,
            "total_amount": 0.0,
            "updated_at": parse_datetime("2023-03-25T18:51:55.597Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_salesorder is not None

    # Handle response
    print(res.accounting_salesorder)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateAccountingSalesorderRequest](../../models/operations/updateaccountingsalesorderrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.UpdateAccountingSalesorderResponse](../../models/operations/updateaccountingsalesorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |