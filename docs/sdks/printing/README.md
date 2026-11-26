# Printing

## Overview

### Available Operations

* [create_printing_file](#create_printing_file) - Create a file
* [create_printing_order](#create_printing_order) - Create an order
* [create_printing_quote](#create_printing_quote) - Create a quote
* [get_printing_file](#get_printing_file) - Retrieve a file
* [get_printing_order](#get_printing_order) - Retrieve an order
* [get_printing_product](#get_printing_product) - Retrieve a product
* [get_printing_template](#get_printing_template) - Retrieve a template
* [list_printing_files](#list_printing_files) - List all files
* [list_printing_orders](#list_printing_orders) - List all orders
* [list_printing_products](#list_printing_products) - List all products
* [list_printing_templates](#list_printing_templates) - List all templates
* [patch_printing_order](#patch_printing_order) - Update an order
* [remove_printing_order](#remove_printing_order) - Remove an order
* [update_printing_order](#update_printing_order) - Update an order

## create_printing_file

Creates a PrintingFile. Provide the unified PrintingFile fields in the request body; they are mapped to the provider's API. Returns the created PrintingFile.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPrintingFile" method="post" path="/printing/{connection_id}/file" example="printing_file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.create_printing_file(request={
        "printing_file": {
            "created_at": parse_datetime("2020-10-22T04:25:39.825Z"),
            "dpi": 300.0,
            "height": 5400.0,
            "id": "c35be3e9-c3be-4478-b0df-b883fb76e24d",
            "metadata": [],
            "mime_type": "image/jpeg",
            "name": "blond-ecliptic.jpg",
            "preview_url": "https://picsum.photos/seed/aATvhmNA/400/400",
            "size": 1956654.0,
            "status": shared.PrintingFileStatus.READY,
            "updated_at": parse_datetime("2020-10-22T04:25:39.825Z"),
            "url": "https://picsum.photos/seed/XBj97B/2783/172",
            "width": 4500.0,
        },
        "connection_id": "<id>",
    })

    assert res.printing_file is not None

    # Handle response
    print(res.printing_file)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreatePrintingFileRequest](../../models/operations/createprintingfilerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreatePrintingFileResponse](../../models/operations/createprintingfileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_printing_order

Creates a PrintingOrder. Provide the unified PrintingOrder fields in the request body; they are mapped to the provider's API. Returns the created PrintingOrder.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPrintingOrder" method="post" path="/printing/{connection_id}/order" example="printing_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.create_printing_order(request={
        "printing_order": {
            "created_at": parse_datetime("2022-03-14T11:16:15.147Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "id": "9d6516d5-784b-4442-9751-127e629dba39",
            "lineitems": [
                {
                    "files": [
                        {
                            "placement": "default",
                            "url": "https://picsum.photos/seed/y54e6o9hYi/191/3357",
                        },
                    ],
                    "id": "1",
                    "name": "Bespoke Marble Chair",
                    "quantity": 2.0,
                    "retail_price_amount": 54.89,
                    "sku": "IBDIE3XR",
                    "unit_price_amount": 26.37,
                },
                {
                    "files": [
                        {
                            "placement": "default",
                            "url": "https://picsum.photos/seed/T7S5xf/3521/1221",
                        },
                    ],
                    "id": "2",
                    "name": "Electronic Cotton Hat",
                    "quantity": 1.0,
                    "retail_price_amount": 23.94,
                    "unit_price_amount": 10.04,
                },
            ],
            "metadata": [],
            "shipments": [],
            "shipping_address": {
                "address1": "651 Main Street",
                "city": "Euclid",
                "country": "United States",
                "country_code": "US",
                "email": "gary_leffler28@gmail.com",
                "name": "Angelita Denesik",
                "postal_code": "80301",
                "region": "Colorado",
                "region_code": "AR",
                "telephone": "808-831-6489 x62979",
            },
            "shipping_amount": 4.69,
            "shipping_method": "STANDARD",
            "status": shared.PrintingOrderStatus.OTHER,
            "subtotal_amount": 62.78,
            "tax_amount": 5.02,
            "total_amount": 72.49,
            "updated_at": parse_datetime("2025-01-23T00:20:58.017Z"),
        },
        "connection_id": "<id>",
    })

    assert res.printing_order is not None

    # Handle response
    print(res.printing_order)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreatePrintingOrderRequest](../../models/operations/createprintingorderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreatePrintingOrderResponse](../../models/operations/createprintingorderresponse.md)**

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

    res = unified_to.printing.create_printing_quote(request={
        "printing_quote": {
            "created_at": parse_datetime("2019-01-02T03:42:06.944Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "id": "c0ca1481-d794-43b1-a1f3-80d0a7364419",
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

## get_printing_file

Retrieves a single PrintingFile by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPrintingFile" method="get" path="/printing/{connection_id}/file/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.get_printing_file(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.printing_file is not None

    # Handle response
    print(res.printing_file)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetPrintingFileRequest](../../models/operations/getprintingfilerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetPrintingFileResponse](../../models/operations/getprintingfileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_printing_order

Retrieves a single PrintingOrder by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPrintingOrder" method="get" path="/printing/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.get_printing_order(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.printing_order is not None

    # Handle response
    print(res.printing_order)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPrintingOrderRequest](../../models/operations/getprintingorderrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetPrintingOrderResponse](../../models/operations/getprintingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_printing_product

Retrieves a single PrintingProduct by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPrintingProduct" method="get" path="/printing/{connection_id}/product/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.get_printing_product(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.printing_product is not None

    # Handle response
    print(res.printing_product)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetPrintingProductRequest](../../models/operations/getprintingproductrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetPrintingProductResponse](../../models/operations/getprintingproductresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_printing_template

Retrieves a single PrintingTemplate by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPrintingTemplate" method="get" path="/printing/{connection_id}/template/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.get_printing_template(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.printing_template is not None

    # Handle response
    print(res.printing_template)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetPrintingTemplateRequest](../../models/operations/getprintingtemplaterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetPrintingTemplateResponse](../../models/operations/getprintingtemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_printing_files

Returns a list of PrintingFiles. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPrintingFiles" method="get" path="/printing/{connection_id}/file" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.list_printing_files(request={
        "connection_id": "<id>",
    })

    assert res.printing_files is not None

    # Handle response
    print(res.printing_files)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListPrintingFilesRequest](../../models/operations/listprintingfilesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListPrintingFilesResponse](../../models/operations/listprintingfilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_printing_orders

Returns a list of PrintingOrders. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPrintingOrders" method="get" path="/printing/{connection_id}/order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.list_printing_orders(request={
        "connection_id": "<id>",
    })

    assert res.printing_orders is not None

    # Handle response
    print(res.printing_orders)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPrintingOrdersRequest](../../models/operations/listprintingordersrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListPrintingOrdersResponse](../../models/operations/listprintingordersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_printing_products

Returns a list of PrintingProducts. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPrintingProducts" method="get" path="/printing/{connection_id}/product" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.list_printing_products(request={
        "connection_id": "<id>",
    })

    assert res.printing_products is not None

    # Handle response
    print(res.printing_products)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListPrintingProductsRequest](../../models/operations/listprintingproductsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListPrintingProductsResponse](../../models/operations/listprintingproductsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_printing_templates

Returns a list of PrintingTemplates. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPrintingTemplates" method="get" path="/printing/{connection_id}/template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.list_printing_templates(request={
        "connection_id": "<id>",
    })

    assert res.printing_templates is not None

    # Handle response
    print(res.printing_templates)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListPrintingTemplatesRequest](../../models/operations/listprintingtemplatesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListPrintingTemplatesResponse](../../models/operations/listprintingtemplatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_printing_order

Updates the PrintingOrder identified by `id`. Provide the unified PrintingOrder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPrintingOrder" method="patch" path="/printing/{connection_id}/order/{id}" example="printing_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.patch_printing_order(request={
        "printing_order": {
            "created_at": parse_datetime("2022-03-14T11:16:15.147Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "id": "af220e4d-5540-45c4-bb37-aeb092251e06",
            "lineitems": [
                {
                    "files": [
                        {
                            "placement": "default",
                            "url": "https://picsum.photos/seed/y54e6o9hYi/191/3357",
                        },
                    ],
                    "id": "1",
                    "name": "Bespoke Marble Chair",
                    "quantity": 2.0,
                    "retail_price_amount": 54.89,
                    "sku": "IBDIE3XR",
                    "unit_price_amount": 26.37,
                },
                {
                    "files": [
                        {
                            "placement": "default",
                            "url": "https://picsum.photos/seed/T7S5xf/3521/1221",
                        },
                    ],
                    "id": "2",
                    "name": "Electronic Cotton Hat",
                    "quantity": 1.0,
                    "retail_price_amount": 23.94,
                    "unit_price_amount": 10.04,
                },
            ],
            "metadata": [],
            "shipments": [],
            "shipping_address": {
                "address1": "651 Main Street",
                "city": "Euclid",
                "country": "United States",
                "country_code": "US",
                "email": "gary_leffler28@gmail.com",
                "name": "Angelita Denesik",
                "postal_code": "80301",
                "region": "Colorado",
                "region_code": "AR",
                "telephone": "808-831-6489 x62979",
            },
            "shipping_amount": 4.69,
            "shipping_method": "STANDARD",
            "status": shared.PrintingOrderStatus.OTHER,
            "subtotal_amount": 62.78,
            "tax_amount": 5.02,
            "total_amount": 72.49,
            "updated_at": parse_datetime("2025-01-23T00:20:58.037Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.printing_order is not None

    # Handle response
    print(res.printing_order)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchPrintingOrderRequest](../../models/operations/patchprintingorderrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchPrintingOrderResponse](../../models/operations/patchprintingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_printing_order

Deletes the PrintingOrder identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removePrintingOrder" method="delete" path="/printing/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.remove_printing_order(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemovePrintingOrderRequest](../../models/operations/removeprintingorderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemovePrintingOrderResponse](../../models/operations/removeprintingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_printing_order

Updates the PrintingOrder identified by `id`. Provide the unified PrintingOrder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePrintingOrder" method="put" path="/printing/{connection_id}/order/{id}" example="printing_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.printing.update_printing_order(request={
        "printing_order": {
            "created_at": parse_datetime("2022-03-14T11:16:15.147Z"),
            "currency": "USD",
            "discount_amount": 0.0,
            "id": "af220e4d-5540-45c4-bb37-aeb092251e06",
            "lineitems": [
                {
                    "files": [
                        {
                            "placement": "default",
                            "url": "https://picsum.photos/seed/y54e6o9hYi/191/3357",
                        },
                    ],
                    "id": "1",
                    "name": "Bespoke Marble Chair",
                    "quantity": 2.0,
                    "retail_price_amount": 54.89,
                    "sku": "IBDIE3XR",
                    "unit_price_amount": 26.37,
                },
                {
                    "files": [
                        {
                            "placement": "default",
                            "url": "https://picsum.photos/seed/T7S5xf/3521/1221",
                        },
                    ],
                    "id": "2",
                    "name": "Electronic Cotton Hat",
                    "quantity": 1.0,
                    "retail_price_amount": 23.94,
                    "unit_price_amount": 10.04,
                },
            ],
            "metadata": [],
            "shipments": [],
            "shipping_address": {
                "address1": "651 Main Street",
                "city": "Euclid",
                "country": "United States",
                "country_code": "US",
                "email": "gary_leffler28@gmail.com",
                "name": "Angelita Denesik",
                "postal_code": "80301",
                "region": "Colorado",
                "region_code": "AR",
                "telephone": "808-831-6489 x62979",
            },
            "shipping_amount": 4.69,
            "shipping_method": "STANDARD",
            "status": shared.PrintingOrderStatus.OTHER,
            "subtotal_amount": 62.78,
            "tax_amount": 5.02,
            "total_amount": 72.49,
            "updated_at": parse_datetime("2025-01-23T00:20:58.037Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.printing_order is not None

    # Handle response
    print(res.printing_order)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdatePrintingOrderRequest](../../models/operations/updateprintingorderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdatePrintingOrderResponse](../../models/operations/updateprintingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |