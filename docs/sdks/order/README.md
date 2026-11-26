# Order

## Overview

### Available Operations

* [~~create_accounting_order~~](#create_accounting_order) - Create an order :warning: **Deprecated**
* [create_assessment_order](#create_assessment_order) - Create an order
* [create_printing_order](#create_printing_order) - Create an order
* [~~get_accounting_order~~](#get_accounting_order) - Retrieve an order :warning: **Deprecated**
* [get_assessment_order](#get_assessment_order) - Retrieve an order
* [get_printing_order](#get_printing_order) - Retrieve an order
* [~~list_accounting_orders~~](#list_accounting_orders) - List all orders :warning: **Deprecated**
* [list_printing_orders](#list_printing_orders) - List all orders
* [~~patch_accounting_order~~](#patch_accounting_order) - Update an order :warning: **Deprecated**
* [patch_assessment_order](#patch_assessment_order) - Update an order
* [patch_printing_order](#patch_printing_order) - Update an order
* [~~remove_accounting_order~~](#remove_accounting_order) - Remove an order :warning: **Deprecated**
* [remove_printing_order](#remove_printing_order) - Remove an order
* [~~update_accounting_order~~](#update_accounting_order) - Update an order :warning: **Deprecated**
* [update_assessment_order](#update_assessment_order) - Update an order
* [update_printing_order](#update_printing_order) - Update an order

## ~~create_accounting_order~~

Creates a AccountingOrder. Provide the unified AccountingOrder fields in the request body; they are mapped to the provider's API. Returns the created AccountingOrder.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAccountingOrder" method="post" path="/accounting/{connection_id}/order" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.create_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "125 Hayden Highway",
                "city": "Altoona",
                "country_code": "US",
                "postal_code": "94706-7691",
                "region": "Louisiana",
                "region_code": "VT",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "2979e2a1-ffd4-4322-8fc3-477ee3de2622",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "450 Garett Mall",
                "city": "New Kamronburgh",
                "country_code": "US",
                "postal_code": "76546",
                "region": "Oregon",
                "region_code": "VA",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-15T17:02:42.994Z"),
        },
        "connection_id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAccountingOrderRequest](../../models/operations/createaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAccountingOrderResponse](../../models/operations/createaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_assessment_order

Creates a AssessmentOrder. Provide the unified AssessmentOrder fields in the request body; they are mapped to the provider's API. Returns the created AssessmentOrder.

### Example Usage

<!-- UsageSnippet language="python" operationID="createAssessmentOrder" method="post" path="/assessment/{connection_id}/order" example="assessment_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.create_assessment_order(request={
        "assessment_order": {
            "connection_id": "",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "0e9aae88-f7b1-44db-9eb7-bae5b1c01c18",
            "metadata": [],
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "jordan.braun@icloud.com",
            ],
            "profile_first_name": "Jordan",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Braun",
            "profile_name": "Jordan Braun",
            "profile_resume_url": "https://astonishing-bug.com/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "322.658.2806 x3159",
            ],
            "reference": "calcar",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 84.0,
            "response_score": 82.0,
            "response_status": shared.ResponseStatus.REJECTED,
            "response_url": "https://nervous-daughter.info/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://idolized-suv.info",
            "updated_at": parse_datetime("2023-02-04T10:05:17.586Z"),
            "workspace_id": "<id>",
        },
        "connection_id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAssessmentOrderRequest](../../models/operations/createassessmentorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateAssessmentOrderResponse](../../models/operations/createassessmentorderresponse.md)**

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

    res = unified_to.order.create_printing_order(request={
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

## ~~get_accounting_order~~

Retrieves a single AccountingOrder by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAccountingOrder" method="get" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.get_accounting_order(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountingOrderRequest](../../models/operations/getaccountingorderrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAccountingOrderResponse](../../models/operations/getaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_assessment_order

Retrieves a single AssessmentOrder by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAssessmentOrder" method="get" path="/assessment/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.get_assessment_order(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAssessmentOrderRequest](../../models/operations/getassessmentorderrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetAssessmentOrderResponse](../../models/operations/getassessmentorderresponse.md)**

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

    res = unified_to.order.get_printing_order(request={
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

## ~~list_accounting_orders~~

Returns a list of AccountingOrders. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="listAccountingOrders" method="get" path="/accounting/{connection_id}/order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.list_accounting_orders(request={
        "connection_id": "<id>",
    })

    assert res.accounting_orders is not None

    # Handle response
    print(res.accounting_orders)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListAccountingOrdersRequest](../../models/operations/listaccountingordersrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListAccountingOrdersResponse](../../models/operations/listaccountingordersresponse.md)**

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

    res = unified_to.order.list_printing_orders(request={
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

## ~~patch_accounting_order~~

Updates the AccountingOrder identified by `id`. Provide the unified AccountingOrder fields to change in the request body.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAccountingOrder" method="patch" path="/accounting/{connection_id}/order/{id}" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.patch_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "125 Hayden Highway",
                "city": "Altoona",
                "country_code": "US",
                "postal_code": "94706-7691",
                "region": "Louisiana",
                "region_code": "VT",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "b048f651-5d88-4b31-b8fd-14f1914ea89f",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "450 Garett Mall",
                "city": "New Kamronburgh",
                "country_code": "US",
                "postal_code": "76546",
                "region": "Oregon",
                "region_code": "VA",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-15T17:02:43.001Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAccountingOrderRequest](../../models/operations/patchaccountingorderrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAccountingOrderResponse](../../models/operations/patchaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_assessment_order

Updates the AssessmentOrder identified by `id`. Provide the unified AssessmentOrder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAssessmentOrder" method="patch" path="/assessment/{connection_id}/order/{id}" example="assessment_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.patch_assessment_order(request={
        "assessment_order": {
            "connection_id": "",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "1fcae33f-aaf4-4fbf-ada4-05639d7c5869",
            "metadata": [],
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "jordan.braun@icloud.com",
            ],
            "profile_first_name": "Jordan",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Braun",
            "profile_name": "Jordan Braun",
            "profile_resume_url": "https://astonishing-bug.com/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "322.658.2806 x3159",
            ],
            "reference": "calcar",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 84.0,
            "response_score": 82.0,
            "response_status": shared.ResponseStatus.REJECTED,
            "response_url": "https://nervous-daughter.info/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://idolized-suv.info",
            "updated_at": parse_datetime("2023-02-04T10:05:17.593Z"),
            "workspace_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchAssessmentOrderRequest](../../models/operations/patchassessmentorderrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchAssessmentOrderResponse](../../models/operations/patchassessmentorderresponse.md)**

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

    res = unified_to.order.patch_printing_order(request={
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

## ~~remove_accounting_order~~

Deletes the AccountingOrder identified by `id`.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAccountingOrder" method="delete" path="/accounting/{connection_id}/order/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.remove_accounting_order(request={
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
| `request`                                                                                          | [operations.RemoveAccountingOrderRequest](../../models/operations/removeaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveAccountingOrderResponse](../../models/operations/removeaccountingorderresponse.md)**

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

    res = unified_to.order.remove_printing_order(request={
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

## ~~update_accounting_order~~

Updates the AccountingOrder identified by `id`. Provide the unified AccountingOrder fields to change in the request body.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAccountingOrder" method="put" path="/accounting/{connection_id}/order/{id}" example="accounting_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.update_accounting_order(request={
        "accounting_order": {
            "billing_address": {
                "address1": "125 Hayden Highway",
                "city": "Altoona",
                "country_code": "US",
                "postal_code": "94706-7691",
                "region": "Louisiana",
                "region_code": "VT",
            },
            "created_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "currency": "GBP",
            "id": "b048f651-5d88-4b31-b8fd-14f1914ea89f",
            "lineitems": [],
            "metadata": [],
            "posted_at": parse_datetime("2020-11-20T03:46:49.837Z"),
            "shipping_address": {
                "address1": "450 Garett Mall",
                "city": "New Kamronburgh",
                "country_code": "US",
                "postal_code": "76546",
                "region": "Oregon",
                "region_code": "VA",
            },
            "status": shared.AccountingOrderStatus.AUTHORIZED,
            "total_amount": 0.0,
            "type": shared.AccountingOrderType.SALES,
            "updated_at": parse_datetime("2022-02-15T17:02:43.001Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.accounting_order is not None

    # Handle response
    print(res.accounting_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAccountingOrderRequest](../../models/operations/updateaccountingorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAccountingOrderResponse](../../models/operations/updateaccountingorderresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_assessment_order

Updates the AssessmentOrder identified by `id`. Provide the unified AssessmentOrder fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAssessmentOrder" method="put" path="/assessment/{connection_id}/order/{id}" example="assessment_order" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.order.update_assessment_order(request={
        "assessment_order": {
            "connection_id": "",
            "created_at": parse_datetime("2021-09-18T10:33:57.803Z"),
            "id": "1fcae33f-aaf4-4fbf-ada4-05639d7c5869",
            "metadata": [],
            "parameters": [],
            "profile_addresses": [],
            "profile_date_of_birth": "1989-07-22T16:18:37.650Z",
            "profile_emails": [
                "jordan.braun@icloud.com",
            ],
            "profile_first_name": "Jordan",
            "profile_gender": shared.ProfileGender.NON_BINARY,
            "profile_last_name": "Braun",
            "profile_name": "Jordan Braun",
            "profile_resume_url": "https://astonishing-bug.com/",
            "profile_social_media_urls": [],
            "profile_telephones": [
                "322.658.2806 x3159",
            ],
            "reference": "calcar",
            "response_attributes": [],
            "response_details": [],
            "response_download_urls": [],
            "response_max_score": 84.0,
            "response_score": 82.0,
            "response_status": shared.ResponseStatus.REJECTED,
            "response_url": "https://nervous-daughter.info/",
            "status": shared.AssessmentOrderStatus.REJECTED,
            "target_url": "https://idolized-suv.info",
            "updated_at": parse_datetime("2023-02-04T10:05:17.593Z"),
            "workspace_id": "<id>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.assessment_order is not None

    # Handle response
    print(res.assessment_order)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateAssessmentOrderRequest](../../models/operations/updateassessmentorderrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateAssessmentOrderResponse](../../models/operations/updateassessmentorderresponse.md)**

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

    res = unified_to.order.update_printing_order(request={
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