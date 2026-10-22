# List

## Overview

### Available Operations

* [create_martech_list](#create_martech_list) - Create a list
* [get_martech_list](#get_martech_list) - Retrieve a list
* [list_martech_lists](#list_martech_lists) - List all lists
* [patch_martech_list](#patch_martech_list) - Update a list
* [remove_martech_list](#remove_martech_list) - Remove a list
* [update_martech_list](#update_martech_list) - Update a list

## create_martech_list

Creates a MarketingList. Provide the unified MarketingList fields in the request body; they are mapped to the provider's API. Returns the created MarketingList.

### Example Usage

<!-- UsageSnippet language="python" operationID="createMartechList" method="post" path="/martech/{connection_id}/list" example="martech_list" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.create_martech_list(request={
        "marketing_list": {
            "address": {
                "address1": "76564 Coronation Road",
                "address2": "Suite 922",
                "city": "West Jordon",
                "country": "Mexico",
                "postal_code": "04183",
                "region": "NC",
            },
            "created_at": parse_datetime("2019-09-18T02:01:36.950Z"),
            "description": "Vilis.",
            "id": "2485bd30-b777-49c0-b8f0-bddbe8d2a0fd",
            "is_active": True,
            "language": "ru",
            "metadata": [],
            "name": "Electronics Newsletter",
            "sender_company": "Koepp and Sons",
            "sender_email": "blake.kuhn@hotmail.com",
            "sender_name": "Blake Kuhn",
            "sender_phone": "359.305.7962 x28115",
            "subject": "Theca caecus copia crebro valeo ulciscor.",
            "updated_at": parse_datetime("2022-09-13T20:09:43.170Z"),
        },
        "connection_id": "<id>",
    })

    assert res.marketing_list is not None

    # Handle response
    print(res.marketing_list)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateMartechListRequest](../../models/operations/createmartechlistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateMartechListResponse](../../models/operations/createmartechlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_martech_list

Retrieves a single MarketingList by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMartechList" method="get" path="/martech/{connection_id}/list/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.get_martech_list(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_list is not None

    # Handle response
    print(res.marketing_list)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetMartechListRequest](../../models/operations/getmartechlistrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetMartechListResponse](../../models/operations/getmartechlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_martech_lists

Returns a list of MarketingLists. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listMartechLists" method="get" path="/martech/{connection_id}/list" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.list_martech_lists(request={
        "connection_id": "<id>",
    })

    assert res.marketing_lists is not None

    # Handle response
    print(res.marketing_lists)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListMartechListsRequest](../../models/operations/listmartechlistsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.ListMartechListsResponse](../../models/operations/listmartechlistsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_martech_list

Updates the MarketingList identified by `id`. Provide the unified MarketingList fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMartechList" method="patch" path="/martech/{connection_id}/list/{id}" example="martech_list" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.patch_martech_list(request={
        "marketing_list": {
            "address": {
                "address1": "76564 Coronation Road",
                "address2": "Suite 922",
                "city": "West Jordon",
                "country": "Mexico",
                "postal_code": "04183",
                "region": "NC",
            },
            "created_at": parse_datetime("2019-09-18T02:01:36.950Z"),
            "description": "Vilis.",
            "id": "0032fa3c-da58-495e-9422-ab015754772d",
            "is_active": True,
            "language": "ru",
            "metadata": [],
            "name": "Electronics Newsletter",
            "sender_company": "Koepp and Sons",
            "sender_email": "blake.kuhn@hotmail.com",
            "sender_name": "Blake Kuhn",
            "sender_phone": "359.305.7962 x28115",
            "subject": "Theca caecus copia crebro valeo ulciscor.",
            "updated_at": parse_datetime("2022-09-13T20:09:43.183Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_list is not None

    # Handle response
    print(res.marketing_list)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchMartechListRequest](../../models/operations/patchmartechlistrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchMartechListResponse](../../models/operations/patchmartechlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_martech_list

Deletes the MarketingList identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMartechList" method="delete" path="/martech/{connection_id}/list/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.remove_martech_list(request={
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
| `request`                                                                                  | [operations.RemoveMartechListRequest](../../models/operations/removemartechlistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveMartechListResponse](../../models/operations/removemartechlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_martech_list

Updates the MarketingList identified by `id`. Provide the unified MarketingList fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMartechList" method="put" path="/martech/{connection_id}/list/{id}" example="martech_list" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.update_martech_list(request={
        "marketing_list": {
            "address": {
                "address1": "76564 Coronation Road",
                "address2": "Suite 922",
                "city": "West Jordon",
                "country": "Mexico",
                "postal_code": "04183",
                "region": "NC",
            },
            "created_at": parse_datetime("2019-09-18T02:01:36.950Z"),
            "description": "Vilis.",
            "id": "0032fa3c-da58-495e-9422-ab015754772d",
            "is_active": True,
            "language": "ru",
            "metadata": [],
            "name": "Electronics Newsletter",
            "sender_company": "Koepp and Sons",
            "sender_email": "blake.kuhn@hotmail.com",
            "sender_name": "Blake Kuhn",
            "sender_phone": "359.305.7962 x28115",
            "subject": "Theca caecus copia crebro valeo ulciscor.",
            "updated_at": parse_datetime("2022-09-13T20:09:43.183Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_list is not None

    # Handle response
    print(res.marketing_list)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateMartechListRequest](../../models/operations/updatemartechlistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateMartechListResponse](../../models/operations/updatemartechlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |