# Link

## Overview

### Available Operations

* [create_calendar_link](#create_calendar_link) - Create a link
* [create_payment_link](#create_payment_link) - Create a link
* [get_calendar_link](#get_calendar_link) - Retrieve a link
* [get_payment_link](#get_payment_link) - Retrieve a link
* [list_calendar_links](#list_calendar_links) - List all links
* [list_payment_links](#list_payment_links) - List all links
* [patch_calendar_link](#patch_calendar_link) - Update a link
* [patch_payment_link](#patch_payment_link) - Update a link
* [remove_calendar_link](#remove_calendar_link) - Remove a link
* [remove_payment_link](#remove_payment_link) - Remove a link
* [update_calendar_link](#update_calendar_link) - Update a link
* [update_payment_link](#update_payment_link) - Update a link

## create_calendar_link

Create a link

### Example Usage

<!-- UsageSnippet language="python" operationID="createCalendarLink" method="post" path="/calendar/{connection_id}/link" example="calendar_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.create_calendar_link(request={
        "calendar_link": {
            "created_at": "2023-03-07T13:34:11.959Z",
            "description": "Vitium clibanus laboriosam uxor denuncio.",
            "duration": 74.0,
            "id": "f0fa59b9-4357-4a4b-a4b4-4db3717fd222",
            "is_active": True,
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-06T14:07:35.943Z",
            "url": "https://annual-apricot.info/",
        },
        "connection_id": "<id>",
    })

    assert res.calendar_link is not None

    # Handle response
    print(res.calendar_link)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateCalendarLinkRequest](../../models/operations/createcalendarlinkrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateCalendarLinkResponse](../../models/operations/createcalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_payment_link

Create a link

### Example Usage

<!-- UsageSnippet language="python" operationID="createPaymentLink" method="post" path="/payment/{connection_id}/link" example="payment_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.create_payment_link(request={
        "payment_link": {
            "amount": 81211.0,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "GYD",
            "description": "Adfero ipsa terreo benevolentia utrum.",
            "id": "37f5d3c2-c021-4fec-af54-3ce154a3a092",
            "is_active": True,
            "is_chargeable_now": False,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-08-21T00:45:53.202Z"),
                    "id": "3e5f9c8d-4bd8-4e27-9a12-e901d131a988",
                    "item_description": "Experience the white brilliance of our Hat, perfect for aggravating environments",
                    "item_name": "Licensed Marble Mouse",
                    "item_sku": "TAD4EYLVRI",
                    "notes": "Charisma theca video verus conduco attollo cervus decretum viridis.",
                    "tax_amount": 221.0,
                    "total_amount": 1841.0,
                    "unit_amount": 270.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-02-12T17:31:25.507Z"),
                },
                {
                    "created_at": parse_datetime("2023-09-30T05:29:29.258Z"),
                    "discount_amount": 15.0,
                    "id": "3a20d8c1-5dfa-4f92-a648-075e8bcfa0d3",
                    "item_description": "New Chicken model with 79 GB RAM, 846 GB storage, and lovely features",
                    "item_name": "Intelligent Steel Table",
                    "item_sku": "V8HQCDQYUZ",
                    "tax_amount": 150.0,
                    "total_amount": 2037.0,
                    "unit_amount": 317.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-05-31T11:10:09.190Z"),
                },
                {
                    "created_at": parse_datetime("2023-12-16T13:52:52.341Z"),
                    "id": "53f45482-602a-4032-ad78-55812c3a9fe0",
                    "item_description": "Dach - Wolff's most advanced Car technology increases dense capabilities",
                    "item_name": "Modern Gold Soap",
                    "item_sku": "DYGKCTCLDJ",
                    "tax_amount": 41.0,
                    "total_amount": 281.0,
                    "unit_amount": 30.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-05-22T16:35:07.583Z"),
                },
                {
                    "created_at": parse_datetime("2023-08-12T19:45:39.705Z"),
                    "id": "edebdd70-ab48-47cc-81c8-b6bba03a550a",
                    "item_description": "The sleek and unimportant Salad comes with salmon LED lighting for smart functionality",
                    "item_name": "Generic Aluminum Ball",
                    "item_sku": "BSBAXWAAFF",
                    "notes": "Cubo adversus victus subito asperiores vereor cibo tabgo.",
                    "tax_amount": 6.0,
                    "total_amount": 78.0,
                    "unit_amount": 24.0,
                    "unit_quantity": 3.0,
                    "updated_at": parse_datetime("2023-11-13T12:39:15.951Z"),
                },
                {
                    "created_at": parse_datetime("2023-02-14T06:21:13.641Z"),
                    "discount_amount": 171.0,
                    "id": "c91006cd-61d8-4b38-948e-afad4f546da0",
                    "item_description": "New Bike model with 29 GB RAM, 271 GB storage, and minty features",
                    "item_name": "Incredible Aluminum Chicken",
                    "item_sku": "6ERMJK20HE",
                    "tax_amount": 263.0,
                    "total_amount": 3708.0,
                    "unit_amount": 452.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-01-31T21:39:30.894Z"),
                },
            ],
            "success_url": "https://parched-kettledrum.com/",
            "updated_at": parse_datetime("2025-12-11T19:12:39.885Z"),
            "url": "https://forceful-laughter.biz/",
        },
        "connection_id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreatePaymentLinkRequest](../../models/operations/createpaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreatePaymentLinkResponse](../../models/operations/createpaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_calendar_link

Retrieve a link

### Example Usage

<!-- UsageSnippet language="python" operationID="getCalendarLink" method="get" path="/calendar/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.get_calendar_link(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_link is not None

    # Handle response
    print(res.calendar_link)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCalendarLinkRequest](../../models/operations/getcalendarlinkrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetCalendarLinkResponse](../../models/operations/getcalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_payment_link

Retrieve a link

### Example Usage

<!-- UsageSnippet language="python" operationID="getPaymentLink" method="get" path="/payment/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.get_payment_link(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetPaymentLinkRequest](../../models/operations/getpaymentlinkrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetPaymentLinkResponse](../../models/operations/getpaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_calendar_links

List all links

### Example Usage

<!-- UsageSnippet language="python" operationID="listCalendarLinks" method="get" path="/calendar/{connection_id}/link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.list_calendar_links(request={
        "connection_id": "<id>",
    })

    assert res.calendar_links is not None

    # Handle response
    print(res.calendar_links)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCalendarLinksRequest](../../models/operations/listcalendarlinksrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListCalendarLinksResponse](../../models/operations/listcalendarlinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_payment_links

List all links

### Example Usage

<!-- UsageSnippet language="python" operationID="listPaymentLinks" method="get" path="/payment/{connection_id}/link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.list_payment_links(request={
        "connection_id": "<id>",
    })

    assert res.payment_links is not None

    # Handle response
    print(res.payment_links)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListPaymentLinksRequest](../../models/operations/listpaymentlinksrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListPaymentLinksResponse](../../models/operations/listpaymentlinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_calendar_link

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCalendarLink" method="patch" path="/calendar/{connection_id}/link/{id}" example="calendar_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.patch_calendar_link(request={
        "calendar_link": {
            "created_at": "2023-03-07T13:34:11.959Z",
            "description": "Vitium clibanus laboriosam uxor denuncio.",
            "duration": 74.0,
            "id": "0876732b-f768-4567-a33b-1cc9e9bfe1d7",
            "is_active": True,
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-06T14:07:35.945Z",
            "url": "https://annual-apricot.info/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_link is not None

    # Handle response
    print(res.calendar_link)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchCalendarLinkRequest](../../models/operations/patchcalendarlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchCalendarLinkResponse](../../models/operations/patchcalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_payment_link

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPaymentLink" method="patch" path="/payment/{connection_id}/link/{id}" example="payment_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.patch_payment_link(request={
        "payment_link": {
            "amount": 81211.0,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "GYD",
            "description": "Adfero ipsa terreo benevolentia utrum.",
            "id": "f5f89ebb-4fa9-42e4-a979-32c088eb9711",
            "is_active": True,
            "is_chargeable_now": False,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-08-21T00:45:53.202Z"),
                    "id": "b828dad9-27f2-4a1b-bc20-93ca9cc1d012",
                    "item_description": "Experience the white brilliance of our Hat, perfect for aggravating environments",
                    "item_name": "Licensed Marble Mouse",
                    "item_sku": "TAD4EYLVRI",
                    "notes": "Charisma theca video verus conduco attollo cervus decretum viridis.",
                    "tax_amount": 221.0,
                    "total_amount": 1841.0,
                    "unit_amount": 270.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-02-12T17:31:25.507Z"),
                },
                {
                    "created_at": parse_datetime("2023-09-30T05:29:29.258Z"),
                    "discount_amount": 15.0,
                    "id": "e614f620-8ef9-4897-951b-157fb8edb78a",
                    "item_description": "New Chicken model with 79 GB RAM, 846 GB storage, and lovely features",
                    "item_name": "Intelligent Steel Table",
                    "item_sku": "V8HQCDQYUZ",
                    "tax_amount": 150.0,
                    "total_amount": 2037.0,
                    "unit_amount": 317.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-05-31T11:10:09.190Z"),
                },
                {
                    "created_at": parse_datetime("2023-12-16T13:52:52.341Z"),
                    "id": "c438ace6-b738-40de-92b3-c8e85c0c8d8a",
                    "item_description": "Dach - Wolff's most advanced Car technology increases dense capabilities",
                    "item_name": "Modern Gold Soap",
                    "item_sku": "DYGKCTCLDJ",
                    "tax_amount": 41.0,
                    "total_amount": 281.0,
                    "unit_amount": 30.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-05-22T16:35:07.583Z"),
                },
                {
                    "created_at": parse_datetime("2023-08-12T19:45:39.705Z"),
                    "id": "335653b4-4475-461d-b754-2f700a624f83",
                    "item_description": "The sleek and unimportant Salad comes with salmon LED lighting for smart functionality",
                    "item_name": "Generic Aluminum Ball",
                    "item_sku": "BSBAXWAAFF",
                    "notes": "Cubo adversus victus subito asperiores vereor cibo tabgo.",
                    "tax_amount": 6.0,
                    "total_amount": 78.0,
                    "unit_amount": 24.0,
                    "unit_quantity": 3.0,
                    "updated_at": parse_datetime("2023-11-13T12:39:15.951Z"),
                },
                {
                    "created_at": parse_datetime("2023-02-14T06:21:13.641Z"),
                    "discount_amount": 171.0,
                    "id": "cd627a38-9375-4f58-ba3a-40ca561a806a",
                    "item_description": "New Bike model with 29 GB RAM, 271 GB storage, and minty features",
                    "item_name": "Incredible Aluminum Chicken",
                    "item_sku": "6ERMJK20HE",
                    "tax_amount": 263.0,
                    "total_amount": 3708.0,
                    "unit_amount": 452.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-01-31T21:39:30.894Z"),
                },
            ],
            "success_url": "https://parched-kettledrum.com/",
            "updated_at": parse_datetime("2025-12-11T19:12:39.895Z"),
            "url": "https://forceful-laughter.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchPaymentLinkRequest](../../models/operations/patchpaymentlinkrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchPaymentLinkResponse](../../models/operations/patchpaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_calendar_link

Remove a link

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCalendarLink" method="delete" path="/calendar/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.remove_calendar_link(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveCalendarLinkRequest](../../models/operations/removecalendarlinkrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveCalendarLinkResponse](../../models/operations/removecalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_payment_link

Remove a link

### Example Usage

<!-- UsageSnippet language="python" operationID="removePaymentLink" method="delete" path="/payment/{connection_id}/link/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.remove_payment_link(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemovePaymentLinkRequest](../../models/operations/removepaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemovePaymentLinkResponse](../../models/operations/removepaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_calendar_link

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCalendarLink" method="put" path="/calendar/{connection_id}/link/{id}" example="calendar_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.update_calendar_link(request={
        "calendar_link": {
            "created_at": "2023-03-07T13:34:11.959Z",
            "description": "Vitium clibanus laboriosam uxor denuncio.",
            "duration": 74.0,
            "id": "0876732b-f768-4567-a33b-1cc9e9bfe1d7",
            "is_active": True,
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-06T14:07:35.945Z",
            "url": "https://annual-apricot.info/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.calendar_link is not None

    # Handle response
    print(res.calendar_link)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateCalendarLinkRequest](../../models/operations/updatecalendarlinkrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateCalendarLinkResponse](../../models/operations/updatecalendarlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_payment_link

Update a link

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePaymentLink" method="put" path="/payment/{connection_id}/link/{id}" example="payment_link" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.link.update_payment_link(request={
        "payment_link": {
            "amount": 81211.0,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "GYD",
            "description": "Adfero ipsa terreo benevolentia utrum.",
            "id": "f5f89ebb-4fa9-42e4-a979-32c088eb9711",
            "is_active": True,
            "is_chargeable_now": False,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-08-21T00:45:53.202Z"),
                    "id": "b828dad9-27f2-4a1b-bc20-93ca9cc1d012",
                    "item_description": "Experience the white brilliance of our Hat, perfect for aggravating environments",
                    "item_name": "Licensed Marble Mouse",
                    "item_sku": "TAD4EYLVRI",
                    "notes": "Charisma theca video verus conduco attollo cervus decretum viridis.",
                    "tax_amount": 221.0,
                    "total_amount": 1841.0,
                    "unit_amount": 270.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-02-12T17:31:25.507Z"),
                },
                {
                    "created_at": parse_datetime("2023-09-30T05:29:29.258Z"),
                    "discount_amount": 15.0,
                    "id": "e614f620-8ef9-4897-951b-157fb8edb78a",
                    "item_description": "New Chicken model with 79 GB RAM, 846 GB storage, and lovely features",
                    "item_name": "Intelligent Steel Table",
                    "item_sku": "V8HQCDQYUZ",
                    "tax_amount": 150.0,
                    "total_amount": 2037.0,
                    "unit_amount": 317.0,
                    "unit_quantity": 6.0,
                    "updated_at": parse_datetime("2023-05-31T11:10:09.190Z"),
                },
                {
                    "created_at": parse_datetime("2023-12-16T13:52:52.341Z"),
                    "id": "c438ace6-b738-40de-92b3-c8e85c0c8d8a",
                    "item_description": "Dach - Wolff's most advanced Car technology increases dense capabilities",
                    "item_name": "Modern Gold Soap",
                    "item_sku": "DYGKCTCLDJ",
                    "tax_amount": 41.0,
                    "total_amount": 281.0,
                    "unit_amount": 30.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-05-22T16:35:07.583Z"),
                },
                {
                    "created_at": parse_datetime("2023-08-12T19:45:39.705Z"),
                    "id": "335653b4-4475-461d-b754-2f700a624f83",
                    "item_description": "The sleek and unimportant Salad comes with salmon LED lighting for smart functionality",
                    "item_name": "Generic Aluminum Ball",
                    "item_sku": "BSBAXWAAFF",
                    "notes": "Cubo adversus victus subito asperiores vereor cibo tabgo.",
                    "tax_amount": 6.0,
                    "total_amount": 78.0,
                    "unit_amount": 24.0,
                    "unit_quantity": 3.0,
                    "updated_at": parse_datetime("2023-11-13T12:39:15.951Z"),
                },
                {
                    "created_at": parse_datetime("2023-02-14T06:21:13.641Z"),
                    "discount_amount": 171.0,
                    "id": "cd627a38-9375-4f58-ba3a-40ca561a806a",
                    "item_description": "New Bike model with 29 GB RAM, 271 GB storage, and minty features",
                    "item_name": "Incredible Aluminum Chicken",
                    "item_sku": "6ERMJK20HE",
                    "tax_amount": 263.0,
                    "total_amount": 3708.0,
                    "unit_amount": 452.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-01-31T21:39:30.894Z"),
                },
            ],
            "success_url": "https://parched-kettledrum.com/",
            "updated_at": parse_datetime("2025-12-11T19:12:39.895Z"),
            "url": "https://forceful-laughter.biz/",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.payment_link is not None

    # Handle response
    print(res.payment_link)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdatePaymentLinkRequest](../../models/operations/updatepaymentlinkrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdatePaymentLinkResponse](../../models/operations/updatepaymentlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |