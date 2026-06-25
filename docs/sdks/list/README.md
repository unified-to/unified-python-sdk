# List

## Overview

### Available Operations

* [create_martech_list2](#create_martech_list2) - Create a list
* [get_martech_list2](#get_martech_list2) - Retrieve a list
* [list_martech_lists2](#list_martech_lists2) - List all lists
* [patch_martech_list2](#patch_martech_list2) - Update a list
* [remove_martech_list2](#remove_martech_list2) - Remove a list
* [update_martech_list2](#update_martech_list2) - Update a list

## create_martech_list2

Create a list

### Example Usage

<!-- UsageSnippet language="python" operationID="createMartechList2" method="post" path="/martech/{connection_id}/list" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.create_martech_list2(request={
        "marketing_list": {},
        "connection_id": "<id>",
    })

    assert res.marketing_list is not None

    # Handle response
    print(res.marketing_list)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateMartechList2Request](../../models/operations/createmartechlist2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateMartechList2Response](../../models/operations/createmartechlist2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_martech_list2

Retrieve a list

### Example Usage

<!-- UsageSnippet language="python" operationID="getMartechList2" method="get" path="/martech/{connection_id}/list/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.get_martech_list2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_list is not None

    # Handle response
    print(res.marketing_list)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetMartechList2Request](../../models/operations/getmartechlist2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetMartechList2Response](../../models/operations/getmartechlist2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_martech_lists2

List all lists

### Example Usage

<!-- UsageSnippet language="python" operationID="listMartechLists2" method="get" path="/martech/{connection_id}/list" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.list_martech_lists2(request={
        "connection_id": "<id>",
    })

    assert res.marketing_lists is not None

    # Handle response
    print(res.marketing_lists)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListMartechLists2Request](../../models/operations/listmartechlists2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListMartechLists2Response](../../models/operations/listmartechlists2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_martech_list2

Update a list

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMartechList2" method="patch" path="/martech/{connection_id}/list/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.patch_martech_list2(request={
        "marketing_list": {},
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
| `request`                                                                                  | [operations.PatchMartechList2Request](../../models/operations/patchmartechlist2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchMartechList2Response](../../models/operations/patchmartechlist2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_martech_list2

Remove a list

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMartechList2" method="delete" path="/martech/{connection_id}/list/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.remove_martech_list2(request={
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
| `request`                                                                                    | [operations.RemoveMartechList2Request](../../models/operations/removemartechlist2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveMartechList2Response](../../models/operations/removemartechlist2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_martech_list2

Update a list

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMartechList2" method="put" path="/martech/{connection_id}/list/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.list.update_martech_list2(request={
        "marketing_list": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.marketing_list is not None

    # Handle response
    print(res.marketing_list)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateMartechList2Request](../../models/operations/updatemartechlist2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateMartechList2Response](../../models/operations/updatemartechlist2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |