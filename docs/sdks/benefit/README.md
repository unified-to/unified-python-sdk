# Benefit

## Overview

### Available Operations

* [create_hris_benefit2](#create_hris_benefit2) - Create a benefit
* [get_hris_benefit2](#get_hris_benefit2) - Retrieve a benefit
* [list_hris_benefits2](#list_hris_benefits2) - List all benefits
* [patch_hris_benefit2](#patch_hris_benefit2) - Update a benefit
* [remove_hris_benefit2](#remove_hris_benefit2) - Remove a benefit
* [update_hris_benefit2](#update_hris_benefit2) - Update a benefit

## create_hris_benefit2

Create a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisBenefit2" method="post" path="/hris/{connection_id}/benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.create_hris_benefit2(request={
        "hris_benefit": {},
        "connection_id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisBenefit2Request](../../models/operations/createhrisbenefit2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisBenefit2Response](../../models/operations/createhrisbenefit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_benefit2

Retrieve a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisBenefit2" method="get" path="/hris/{connection_id}/benefit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.get_hris_benefit2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisBenefit2Request](../../models/operations/gethrisbenefit2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisBenefit2Response](../../models/operations/gethrisbenefit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_benefits2

List all benefits

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisBenefits2" method="get" path="/hris/{connection_id}/benefit" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.list_hris_benefits2(request={
        "connection_id": "<id>",
    })

    assert res.hris_benefits is not None

    # Handle response
    print(res.hris_benefits)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListHrisBenefits2Request](../../models/operations/listhrisbenefits2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListHrisBenefits2Response](../../models/operations/listhrisbenefits2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_benefit2

Update a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisBenefit2" method="patch" path="/hris/{connection_id}/benefit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.patch_hris_benefit2(request={
        "hris_benefit": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisBenefit2Request](../../models/operations/patchhrisbenefit2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisBenefit2Response](../../models/operations/patchhrisbenefit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_benefit2

Remove a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisBenefit2" method="delete" path="/hris/{connection_id}/benefit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.remove_hris_benefit2(request={
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
| `request`                                                                                    | [operations.RemoveHrisBenefit2Request](../../models/operations/removehrisbenefit2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisBenefit2Response](../../models/operations/removehrisbenefit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_benefit2

Update a benefit

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisBenefit2" method="put" path="/hris/{connection_id}/benefit/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.benefit.update_hris_benefit2(request={
        "hris_benefit": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_benefit is not None

    # Handle response
    print(res.hris_benefit)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisBenefit2Request](../../models/operations/updatehrisbenefit2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisBenefit2Response](../../models/operations/updatehrisbenefit2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |