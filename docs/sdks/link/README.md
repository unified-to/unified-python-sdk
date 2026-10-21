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
            "id": "a0594e03-9254-408a-85bd-18efd183d321",
            "is_active": True,
            "metadata": [],
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-15T13:00:32.317Z",
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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "b78627ec-3001-412f-a577-0630fd5e9512",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "958fa847-7deb-4984-a216-0ae8479df9f1",
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
                    "id": "e67c0838-50ab-4933-a381-32a177bb0f83",
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
                    "id": "02a3155b-193e-4f22-8e39-7e057e75fc79",
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
            "updated_at": parse_datetime("2024-04-13T09:30:09.988Z"),
            "url": "https://pay.example.com/b78627ec-3001-412f-a577-0630fd5e9512",
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
            "id": "90dbcdc3-0e37-4df5-8f47-98f71e2aeb87",
            "is_active": True,
            "metadata": [],
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-15T13:00:32.321Z",
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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "0c4720a8-7e94-4f22-bb38-adae3c25b5d0",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "5c02f8fb-c6e9-4e59-a24c-c1b9ce61745b",
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
                    "id": "c54b9cb5-b822-4429-9e14-888d068fbfe6",
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
                    "id": "5db96022-15e7-4c95-8ea5-0fc69f6de9e6",
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
            "updated_at": parse_datetime("2024-04-13T09:30:09.994Z"),
            "url": "https://pay.example.com/0c4720a8-7e94-4f22-bb38-adae3c25b5d0",
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
            "id": "90dbcdc3-0e37-4df5-8f47-98f71e2aeb87",
            "is_active": True,
            "metadata": [],
            "name": "Sopor sopor ancilla animus anser dignissimos vito confero utilis.",
            "price_amount": 44.0,
            "price_currency": "USD",
            "updated_at": "2024-03-15T13:00:32.321Z",
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
            "amount": 17001.68,
            "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
            "currency": "CAD",
            "description": "Savor the tender essence in our Ball, designed for dim culinary adventures",
            "id": "0c4720a8-7e94-4f22-bb38-adae3c25b5d0",
            "is_active": True,
            "is_chargeable_now": True,
            "lineitems": [
                {
                    "created_at": parse_datetime("2023-06-04T16:11:45.685Z"),
                    "id": "5c02f8fb-c6e9-4e59-a24c-c1b9ce61745b",
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
                    "id": "c54b9cb5-b822-4429-9e14-888d068fbfe6",
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
                    "id": "5db96022-15e7-4c95-8ea5-0fc69f6de9e6",
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
            "updated_at": parse_datetime("2024-04-13T09:30:09.994Z"),
            "url": "https://pay.example.com/0c4720a8-7e94-4f22-bb38-adae3c25b5d0",
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