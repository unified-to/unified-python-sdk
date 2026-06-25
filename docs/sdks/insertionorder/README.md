# Insertionorder

## Overview

### Available Operations

* [create_ads_insertionorder2](#create_ads_insertionorder2) - Create an insertionorder
* [get_ads_insertionorder2](#get_ads_insertionorder2) - Retrieve an insertionorder
* [list_ads_insertionorders2](#list_ads_insertionorders2) - List all insertionorders
* [patch_ads_insertionorder2](#patch_ads_insertionorder2) - Update an insertionorder
* [remove_ads_insertionorder2](#remove_ads_insertionorder2) - Remove an insertionorder
* [update_ads_insertionorder2](#update_ads_insertionorder2) - Update an insertionorder

## create_ads_insertionorder2

Create an insertionorder

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdsInsertionorder2" method="post" path="/ads/{connection_id}/insertionorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.insertionorder.create_ads_insertionorder2(request={
        "ads_insertionorder": {},
        "connection_id": "<id>",
    })

    assert res.ads_insertionorder is not None

    # Handle response
    print(res.ads_insertionorder)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateAdsInsertionorder2Request](../../models/operations/createadsinsertionorder2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateAdsInsertionorder2Response](../../models/operations/createadsinsertionorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_ads_insertionorder2

Retrieve an insertionorder

### Example Usage

<!-- UsageSnippet language="python" operationID="getAdsInsertionorder2" method="get" path="/ads/{connection_id}/insertionorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.insertionorder.get_ads_insertionorder2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_insertionorder is not None

    # Handle response
    print(res.ads_insertionorder)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAdsInsertionorder2Request](../../models/operations/getadsinsertionorder2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetAdsInsertionorder2Response](../../models/operations/getadsinsertionorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ads_insertionorders2

List all insertionorders

### Example Usage

<!-- UsageSnippet language="python" operationID="listAdsInsertionorders2" method="get" path="/ads/{connection_id}/insertionorder" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.insertionorder.list_ads_insertionorders2(request={
        "connection_id": "<id>",
    })

    assert res.ads_insertionorders is not None

    # Handle response
    print(res.ads_insertionorders)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListAdsInsertionorders2Request](../../models/operations/listadsinsertionorders2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListAdsInsertionorders2Response](../../models/operations/listadsinsertionorders2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_ads_insertionorder2

Update an insertionorder

### Example Usage

<!-- UsageSnippet language="python" operationID="patchAdsInsertionorder2" method="patch" path="/ads/{connection_id}/insertionorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.insertionorder.patch_ads_insertionorder2(request={
        "ads_insertionorder": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_insertionorder is not None

    # Handle response
    print(res.ads_insertionorder)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchAdsInsertionorder2Request](../../models/operations/patchadsinsertionorder2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.PatchAdsInsertionorder2Response](../../models/operations/patchadsinsertionorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_ads_insertionorder2

Remove an insertionorder

### Example Usage

<!-- UsageSnippet language="python" operationID="removeAdsInsertionorder2" method="delete" path="/ads/{connection_id}/insertionorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.insertionorder.remove_ads_insertionorder2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveAdsInsertionorder2Request](../../models/operations/removeadsinsertionorder2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveAdsInsertionorder2Response](../../models/operations/removeadsinsertionorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_ads_insertionorder2

Update an insertionorder

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdsInsertionorder2" method="put" path="/ads/{connection_id}/insertionorder/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.insertionorder.update_ads_insertionorder2(request={
        "ads_insertionorder": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.ads_insertionorder is not None

    # Handle response
    print(res.ads_insertionorder)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateAdsInsertionorder2Request](../../models/operations/updateadsinsertionorder2request.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.UpdateAdsInsertionorder2Response](../../models/operations/updateadsinsertionorder2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |