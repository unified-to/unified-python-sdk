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

Create a list

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
                "address1": "922 Elmore Manor",
                "address2": "Suite 925",
                "city": "Deerfield Beach",
                "country": "Bahrain",
                "postal_code": "30765-6471",
                "region": "FL",
            },
            "created_at": parse_datetime("2019-09-18T02:01:36.950Z"),
            "description": "Currus.",
            "id": "3657185e-1109-4415-9062-8b017fbc9a88",
            "is_active": True,
            "language": "it",
            "name": "Annette Nolan",
            "sender_company": "Hickle - Homenick",
            "sender_email": "Matt_Steuber@hotmail.com",
            "sender_name": "Salvatore Roob",
            "sender_phone": "896-328-1153 x4957",
            "subject": "Tenetur thymum circumvenio triumphus celo.",
            "updated_at": parse_datetime("2022-08-30T21:48:13.076Z"),
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

Retrieve a list

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

List all lists

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

Update a list

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
                "address1": "922 Elmore Manor",
                "address2": "Suite 925",
                "city": "Deerfield Beach",
                "country": "Bahrain",
                "postal_code": "30765-6471",
                "region": "FL",
            },
            "created_at": parse_datetime("2019-09-18T02:01:36.950Z"),
            "description": "Currus.",
            "id": "a147cd5e-69a2-4ae6-8834-4d91377d97e2",
            "is_active": True,
            "language": "it",
            "name": "Annette Nolan",
            "sender_company": "Hickle - Homenick",
            "sender_email": "Matt_Steuber@hotmail.com",
            "sender_name": "Salvatore Roob",
            "sender_phone": "896-328-1153 x4957",
            "subject": "Tenetur thymum circumvenio triumphus celo.",
            "updated_at": parse_datetime("2022-08-30T21:48:13.081Z"),
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

Remove a list

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

Update a list

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
                "address1": "922 Elmore Manor",
                "address2": "Suite 925",
                "city": "Deerfield Beach",
                "country": "Bahrain",
                "postal_code": "30765-6471",
                "region": "FL",
            },
            "created_at": parse_datetime("2019-09-18T02:01:36.950Z"),
            "description": "Currus.",
            "id": "a147cd5e-69a2-4ae6-8834-4d91377d97e2",
            "is_active": True,
            "language": "it",
            "name": "Annette Nolan",
            "sender_company": "Hickle - Homenick",
            "sender_email": "Matt_Steuber@hotmail.com",
            "sender_name": "Salvatore Roob",
            "sender_phone": "896-328-1153 x4957",
            "subject": "Tenetur thymum circumvenio triumphus celo.",
            "updated_at": parse_datetime("2022-08-30T21:48:13.081Z"),
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