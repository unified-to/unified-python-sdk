# Bankaccount

## Overview

### Available Operations

* [create_hris_bankaccount2](#create_hris_bankaccount2) - Create a bankaccount
* [get_hris_bankaccount2](#get_hris_bankaccount2) - Retrieve a bankaccount
* [list_hris_bankaccounts2](#list_hris_bankaccounts2) - List all bankaccounts
* [patch_hris_bankaccount2](#patch_hris_bankaccount2) - Update a bankaccount
* [remove_hris_bankaccount2](#remove_hris_bankaccount2) - Remove a bankaccount
* [update_hris_bankaccount2](#update_hris_bankaccount2) - Update a bankaccount

## create_hris_bankaccount2

Create a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisBankaccount2" method="post" path="/hris/{connection_id}/bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.create_hris_bankaccount2(request={
        "hris_bankaccount": {},
        "connection_id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateHrisBankaccount2Request](../../models/operations/createhrisbankaccount2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateHrisBankaccount2Response](../../models/operations/createhrisbankaccount2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_bankaccount2

Retrieve a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisBankaccount2" method="get" path="/hris/{connection_id}/bankaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.get_hris_bankaccount2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetHrisBankaccount2Request](../../models/operations/gethrisbankaccount2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetHrisBankaccount2Response](../../models/operations/gethrisbankaccount2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_bankaccounts2

List all bankaccounts

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisBankaccounts2" method="get" path="/hris/{connection_id}/bankaccount" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.list_hris_bankaccounts2(request={
        "connection_id": "<id>",
    })

    assert res.hris_bankaccounts is not None

    # Handle response
    print(res.hris_bankaccounts)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListHrisBankaccounts2Request](../../models/operations/listhrisbankaccounts2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListHrisBankaccounts2Response](../../models/operations/listhrisbankaccounts2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_bankaccount2

Update a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisBankaccount2" method="patch" path="/hris/{connection_id}/bankaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.patch_hris_bankaccount2(request={
        "hris_bankaccount": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchHrisBankaccount2Request](../../models/operations/patchhrisbankaccount2request.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchHrisBankaccount2Response](../../models/operations/patchhrisbankaccount2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_bankaccount2

Remove a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisBankaccount2" method="delete" path="/hris/{connection_id}/bankaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.remove_hris_bankaccount2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveHrisBankaccount2Request](../../models/operations/removehrisbankaccount2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveHrisBankaccount2Response](../../models/operations/removehrisbankaccount2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_bankaccount2

Update a bankaccount

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisBankaccount2" method="put" path="/hris/{connection_id}/bankaccount/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.bankaccount.update_hris_bankaccount2(request={
        "hris_bankaccount": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_bankaccount is not None

    # Handle response
    print(res.hris_bankaccount)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateHrisBankaccount2Request](../../models/operations/updatehrisbankaccount2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateHrisBankaccount2Response](../../models/operations/updatehrisbankaccount2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |