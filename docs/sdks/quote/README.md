# Quote

## Overview

### Available Operations

* [create_accounting_quote](#create_accounting_quote) - Create a quote
* [create_printing_quote](#create_printing_quote) - Create a quote
* [create_property_quote](#create_property_quote) - Create a quote
* [get_accounting_quote](#get_accounting_quote) - Retrieve a quote
* [list_accounting_quotes](#list_accounting_quotes) - List all quotes
* [patch_accounting_quote](#patch_accounting_quote) - Update a quote
* [remove_accounting_quote](#remove_accounting_quote) - Remove a quote
* [update_accounting_quote](#update_accounting_quote) - Update a quote

## create_accounting_quote

Creates a AccountingQuote. Provide the unified AccountingQuote fields in the request body; they are mapped to the provider's API. Returns the created AccountingQuote.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingQuote" method="post" path="/accounting/{connection_id}/quote" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.quote.create_accounting_quote(request={
        "accounting_quote": {},
        "connection_id": "<id>",
    })

    assert res.accounting_quote is not None

    # Handle response
    print(res.accounting_quote)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAccountingQuoteRequest](../../models/operations/createaccountingquoterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAccountingQuoteResponse](../../models/operations/createaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_printing_quote

Creates a PrintingQuote. Provide the unified PrintingQuote fields in the request body; they are mapped to the provider's API. Returns the created PrintingQuote.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPrintingQuote" method="post" path="/printing/{connection_id}/quote" example="printing_quote" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.quote.create_printing_quote(request={
        "printing_quote": {
            "created_at": parse_datetime("2019-01-02T03:42:06.944Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "id": "93ef03f5-a801-4ddf-a541-a7786a1058ed",
            "lineitems": [
                {
                    "files": [
                        {
                            "placement": "default",
                            "url": "https://picsum.photos/seed/0Y5Bjnoiwx/3057/3113",
                        },
                    ],
                    "id": "1",
                    "name": "Practical Wooden Salad",
                    "quantity": 2.0,
                    "retail_price_amount": 50.83,
                    "unit_price_amount": 21.72,
                },
                {
                    "files": [
                        {
                            "placement": "default",
                            "url": "https://picsum.photos/seed/rcPUF/2295/1801",
                        },
                    ],
                    "id": "2",
                    "name": "Handmade Gold Car",
                    "quantity": 4.0,
                    "retail_price_amount": 35.47,
                    "sku": "I79GIBCK",
                    "unit_price_amount": 17.64,
                },
            ],
            "metadata": [],
            "shipping_address": {
                "address1": "4290 Garden Street",
                "address2": "Suite 874",
                "city": "Cartwrightshire",
                "company_name": "Kris and Sons",
                "country": "United States",
                "country_code": "US",
                "email": "jada73@hotmail.com",
                "name": "Heaven Crist",
                "postal_code": "92871",
                "region": "North Carolina",
                "region_code": "KY",
                "telephone": "653.412.8900 x9387",
            },
            "shipping_amount": 4.69,
            "shipping_method": "STANDARD",
            "shipping_options": [
                {
                    "amount": 4.69,
                    "code": "STANDARD",
                    "currency": "USD",
                    "max_delivery_days": 5.0,
                    "min_delivery_days": 3.0,
                    "name": "Flat Rate (3-5 business days after fulfillment)",
                },
                {
                    "amount": 12.99,
                    "code": "EXPRESS",
                    "currency": "USD",
                    "max_delivery_days": 3.0,
                    "min_delivery_days": 1.0,
                    "name": "Express (1-3 business days after fulfillment)",
                },
            ],
            "subtotal_amount": 114.0,
            "tax_amount": 9.12,
            "total_amount": 127.81,
            "updated_at": parse_datetime("2019-01-02T03:42:06.944Z"),
        },
        "connection_id": "<id>",
    })

    assert res.printing_quote is not None

    # Handle response
    print(res.printing_quote)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreatePrintingQuoteRequest](../../models/operations/createprintingquoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreatePrintingQuoteResponse](../../models/operations/createprintingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_property_quote

Creates a PropertyQuote. Provide the unified PropertyQuote fields in the request body; they are mapped to the provider's API. Returns the created PropertyQuote.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPropertyQuote" method="post" path="/property/{connection_id}/quote" example="property_quote" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.quote.create_property_quote(request={
        "property_quote": {
            "adults": 1.0,
            "children": 1.0,
            "created_at": parse_datetime("2020-12-18T19:14:11.415Z"),
            "currency": "USD",
            "deposit_amount": 594.54,
            "end_at": parse_datetime("2026-12-11"),
            "guests": 2.0,
            "id": "f47105fe-9f56-4cf5-bddd-9d5518704fc8",
            "line_items": [
                {
                    "amount": 1665.0,
                    "description": "9 nights",
                    "is_mandatory": True,
                    "name": "Accommodation",
                    "type": shared.PropertyLineitemType.BASE,
                },
                {
                    "amount": 117.0,
                    "is_mandatory": True,
                    "name": "Cleaning fee",
                    "type": shared.PropertyLineitemType.FEE,
                },
                {
                    "amount": 199.8,
                    "is_mandatory": True,
                    "name": "Lodging tax",
                    "type": shared.PropertyLineitemType.TAX,
                },
            ],
            "start_at": parse_datetime("2026-12-02"),
            "total_amount": 1981.8,
        },
        "connection_id": "<id>",
    })

    assert res.property_quote is not None

    # Handle response
    print(res.property_quote)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreatePropertyQuoteRequest](../../models/operations/createpropertyquoterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreatePropertyQuoteResponse](../../models/operations/createpropertyquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_accounting_quote

Retrieves a single AccountingQuote by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingQuote" method="get" path="/accounting/{connection_id}/quote/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.quote.get_accounting_quote(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_quote is not None

    # Handle response
    print(res.accounting_quote)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountingQuoteRequest](../../models/operations/getaccountingquoterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAccountingQuoteResponse](../../models/operations/getaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_accounting_quotes

Returns a list of AccountingQuotes. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingQuotes" method="get" path="/accounting/{connection_id}/quote" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.quote.list_accounting_quotes(request={
        "connection_id": "<id>",
    })

    assert res.accounting_quotes is not None

    # Handle response
    print(res.accounting_quotes)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAccountingQuotesRequest](../../models/operations/listaccountingquotesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAccountingQuotesResponse](../../models/operations/listaccountingquotesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_accounting_quote

Updates the AccountingQuote identified by `id`. Provide the unified AccountingQuote fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingQuote" method="patch" path="/accounting/{connection_id}/quote/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.quote.patch_accounting_quote(request={
        "accounting_quote": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_quote is not None

    # Handle response
    print(res.accounting_quote)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAccountingQuoteRequest](../../models/operations/patchaccountingquoterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAccountingQuoteResponse](../../models/operations/patchaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_accounting_quote

Deletes the AccountingQuote identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingQuote" method="delete" path="/accounting/{connection_id}/quote/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.quote.remove_accounting_quote(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveAccountingQuoteRequest](../../models/operations/removeaccountingquoterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveAccountingQuoteResponse](../../models/operations/removeaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_accounting_quote

Updates the AccountingQuote identified by `id`. Provide the unified AccountingQuote fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingQuote" method="put" path="/accounting/{connection_id}/quote/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.quote.update_accounting_quote(request={
        "accounting_quote": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_quote is not None

    # Handle response
    print(res.accounting_quote)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAccountingQuoteRequest](../../models/operations/updateaccountingquoterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAccountingQuoteResponse](../../models/operations/updateaccountingquoteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |