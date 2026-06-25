# Space

## Overview

### Available Operations

* [create_kms_space2](#create_kms_space2) - Create a space
* [get_kms_space2](#get_kms_space2) - Retrieve a space
* [list_kms_spaces2](#list_kms_spaces2) - List all spaces
* [patch_kms_space2](#patch_kms_space2) - Update a space
* [remove_kms_space2](#remove_kms_space2) - Remove a space
* [update_kms_space2](#update_kms_space2) - Update a space

## create_kms_space2

Create a space

### Example Usage

<!-- UsageSnippet language="python" operationID="createKmsSpace2" method="post" path="/kms/{connection_id}/space" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.space.create_kms_space2(request={
        "kms_space": {},
        "connection_id": "<id>",
    })

    assert res.kms_space is not None

    # Handle response
    print(res.kms_space)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateKmsSpace2Request](../../models/operations/createkmsspace2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateKmsSpace2Response](../../models/operations/createkmsspace2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_kms_space2

Retrieve a space

### Example Usage

<!-- UsageSnippet language="python" operationID="getKmsSpace2" method="get" path="/kms/{connection_id}/space/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.space.get_kms_space2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_space is not None

    # Handle response
    print(res.kms_space)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetKmsSpace2Request](../../models/operations/getkmsspace2request.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetKmsSpace2Response](../../models/operations/getkmsspace2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_kms_spaces2

List all spaces

### Example Usage

<!-- UsageSnippet language="python" operationID="listKmsSpaces2" method="get" path="/kms/{connection_id}/space" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.space.list_kms_spaces2(request={
        "connection_id": "<id>",
    })

    assert res.kms_spaces is not None

    # Handle response
    print(res.kms_spaces)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListKmsSpaces2Request](../../models/operations/listkmsspaces2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListKmsSpaces2Response](../../models/operations/listkmsspaces2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_kms_space2

Update a space

### Example Usage

<!-- UsageSnippet language="python" operationID="patchKmsSpace2" method="patch" path="/kms/{connection_id}/space/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.space.patch_kms_space2(request={
        "kms_space": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_space is not None

    # Handle response
    print(res.kms_space)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchKmsSpace2Request](../../models/operations/patchkmsspace2request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchKmsSpace2Response](../../models/operations/patchkmsspace2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_kms_space2

Remove a space

### Example Usage

<!-- UsageSnippet language="python" operationID="removeKmsSpace2" method="delete" path="/kms/{connection_id}/space/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.space.remove_kms_space2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveKmsSpace2Request](../../models/operations/removekmsspace2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveKmsSpace2Response](../../models/operations/removekmsspace2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_kms_space2

Update a space

### Example Usage

<!-- UsageSnippet language="python" operationID="updateKmsSpace2" method="put" path="/kms/{connection_id}/space/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.space.update_kms_space2(request={
        "kms_space": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.kms_space is not None

    # Handle response
    print(res.kms_space)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateKmsSpace2Request](../../models/operations/updatekmsspace2request.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateKmsSpace2Response](../../models/operations/updatekmsspace2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |