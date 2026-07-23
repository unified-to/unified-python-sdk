# Activation

## Overview

### Available Operations

* [create_cdp_activation](#create_cdp_activation) - Create an activation
* [get_cdp_activation](#get_cdp_activation) - Retrieve an activation
* [list_cdp_activations](#list_cdp_activations) - List all activations
* [patch_cdp_activation](#patch_cdp_activation) - Update an activation
* [remove_cdp_activation](#remove_cdp_activation) - Remove an activation
* [update_cdp_activation](#update_cdp_activation) - Update an activation

## create_cdp_activation

Create an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpActivation" method="post" path="/cdp/{connection_id}/activation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activation.create_cdp_activation(request={
        "cdp_activation": {},
        "connection_id": "<id>",
    })

    assert res.cdp_activation is not None

    # Handle response
    print(res.cdp_activation)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateCdpActivationRequest](../../models/operations/createcdpactivationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateCdpActivationResponse](../../models/operations/createcdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_activation

Retrieve an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpActivation" method="get" path="/cdp/{connection_id}/activation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activation.get_cdp_activation(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_activation is not None

    # Handle response
    print(res.cdp_activation)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCdpActivationRequest](../../models/operations/getcdpactivationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetCdpActivationResponse](../../models/operations/getcdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_activations

List all activations

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpActivations" method="get" path="/cdp/{connection_id}/activation" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activation.list_cdp_activations(request={
        "connection_id": "<id>",
    })

    assert res.cdp_activations is not None

    # Handle response
    print(res.cdp_activations)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListCdpActivationsRequest](../../models/operations/listcdpactivationsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListCdpActivationsResponse](../../models/operations/listcdpactivationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_activation

Update an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpActivation" method="patch" path="/cdp/{connection_id}/activation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activation.patch_cdp_activation(request={
        "cdp_activation": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_activation is not None

    # Handle response
    print(res.cdp_activation)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchCdpActivationRequest](../../models/operations/patchcdpactivationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchCdpActivationResponse](../../models/operations/patchcdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_activation

Remove an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpActivation" method="delete" path="/cdp/{connection_id}/activation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activation.remove_cdp_activation(request={
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
| `request`                                                                                      | [operations.RemoveCdpActivationRequest](../../models/operations/removecdpactivationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveCdpActivationResponse](../../models/operations/removecdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_activation

Update an activation

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpActivation" method="put" path="/cdp/{connection_id}/activation/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.activation.update_cdp_activation(request={
        "cdp_activation": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_activation is not None

    # Handle response
    print(res.cdp_activation)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateCdpActivationRequest](../../models/operations/updatecdpactivationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateCdpActivationResponse](../../models/operations/updatecdpactivationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |