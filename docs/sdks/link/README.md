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

Creates a CalendarLink. Provide the unified CalendarLink fields in the request body; they are mapped to the provider's API. Returns the created CalendarLink.

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
            "id": "2a74e4fa-68fd-45ef-87e8-abb2e8ce4344",
            "is_active": True,
            "metadata": [],
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-18T08:09:47.831Z",
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

Creates a PaymentLink. Provide the unified PaymentLink fields in the request body; they are mapped to the provider's API. Returns the created PaymentLink.

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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "ba1652c8-0e98-428f-969b-f3d4882fdf1c",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "59fff449-b761-4d95-879d-694dcf954bc9",
                    "item_description": "Discover the worst new Computer with an exciting mix of Steel ingredients",
                    "item_name": "Soft Marble Cheese",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "2df6bb07-d260-4b9c-bdd4-5453250d7c8a",
                    "item_description": "Innovative Shoes featuring utilized technology and Cotton construction",
                    "item_name": "Sleek Aluminum Shoes",
                    "notes": "Cervus decretum viridis doloremque.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "7132e147-fec3-4fbe-afbf-383014bd2d1f",
                    "item_description": "Featuring Osmium-enhanced technology, our Soap offers unparalleled major performance",
                    "item_name": "Elegant Concrete Gloves",
                    "notes": "Desipio usque vacuus currus cetera testimonium.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://tinted-jet.info",
            "updated_at": parse_datetime("2024-04-15T21:54:14.795Z"),
            "url": "https://pay.example.com/ba1652c8-0e98-428f-969b-f3d4882fdf1c",
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

Retrieves a single CalendarLink by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Retrieves a single PaymentLink by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

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

Returns a list of CalendarLinks. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Returns a list of PaymentLinks. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

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

Updates the CalendarLink identified by `id`. Provide the unified CalendarLink fields to change in the request body.

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
            "id": "01a8d3c1-b3bf-4bf5-9f04-8262ceee5e49",
            "is_active": True,
            "metadata": [],
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-18T08:09:47.836Z",
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

Updates the PaymentLink identified by `id`. Provide the unified PaymentLink fields to change in the request body.

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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "66b60222-6939-4c3b-aa3c-7e5bc6545d5f",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "b89ab2c4-35bd-4994-ab55-f07d3810132c",
                    "item_description": "Discover the worst new Computer with an exciting mix of Steel ingredients",
                    "item_name": "Soft Marble Cheese",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "13cd0893-ad05-4b01-a006-bfe9eae72f6f",
                    "item_description": "Innovative Shoes featuring utilized technology and Cotton construction",
                    "item_name": "Sleek Aluminum Shoes",
                    "notes": "Cervus decretum viridis doloremque.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "c15475ce-d59e-4b85-9991-fcc38f52a693",
                    "item_description": "Featuring Osmium-enhanced technology, our Soap offers unparalleled major performance",
                    "item_name": "Elegant Concrete Gloves",
                    "notes": "Desipio usque vacuus currus cetera testimonium.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://tinted-jet.info",
            "updated_at": parse_datetime("2024-04-15T21:54:14.799Z"),
            "url": "https://pay.example.com/66b60222-6939-4c3b-aa3c-7e5bc6545d5f",
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

Deletes the CalendarLink identified by `id`.

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

Deletes the PaymentLink identified by `id`.

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

Updates the CalendarLink identified by `id`. Provide the unified CalendarLink fields to change in the request body.

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
            "id": "01a8d3c1-b3bf-4bf5-9f04-8262ceee5e49",
            "is_active": True,
            "metadata": [],
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-18T08:09:47.836Z",
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

Updates the PaymentLink identified by `id`. Provide the unified PaymentLink fields to change in the request body.

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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "66b60222-6939-4c3b-aa3c-7e5bc6545d5f",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "b89ab2c4-35bd-4994-ab55-f07d3810132c",
                    "item_description": "Discover the worst new Computer with an exciting mix of Steel ingredients",
                    "item_name": "Soft Marble Cheese",
                    "tax_amount": 0.0,
                    "total_amount": 9342.0,
                    "unit_amount": 519.0,
                    "unit_quantity": 18.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "discount_amount": 424.32,
                    "id": "13cd0893-ad05-4b01-a006-bfe9eae72f6f",
                    "item_description": "Innovative Shoes featuring utilized technology and Cotton construction",
                    "item_name": "Sleek Aluminum Shoes",
                    "notes": "Cervus decretum viridis doloremque.",
                    "tax_amount": 0.0,
                    "total_amount": 6647.68,
                    "unit_amount": 884.0,
                    "unit_quantity": 8.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "c15475ce-d59e-4b85-9991-fcc38f52a693",
                    "item_description": "Featuring Osmium-enhanced technology, our Soap offers unparalleled major performance",
                    "item_name": "Elegant Concrete Gloves",
                    "notes": "Desipio usque vacuus currus cetera testimonium.",
                    "tax_amount": 0.0,
                    "total_amount": 1012.0,
                    "unit_amount": 506.0,
                    "unit_quantity": 2.0,
                    "updated_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                },
            ],
            "metadata": [],
            "success_url": "https://tinted-jet.info",
            "updated_at": parse_datetime("2024-04-15T21:54:14.799Z"),
            "url": "https://pay.example.com/66b60222-6939-4c3b-aa3c-7e5bc6545d5f",
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