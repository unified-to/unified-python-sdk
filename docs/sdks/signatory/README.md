# Signatory

## Overview

### Available Operations

* [create_signing_signatory2](#create_signing_signatory2) - Create a signatory
* [get_signing_signatory2](#get_signing_signatory2) - Retrieve a signatory
* [list_signing_signatories2](#list_signing_signatories2) - List all signatories
* [patch_signing_signatory2](#patch_signing_signatory2) - Update a signatory
* [remove_signing_signatory2](#remove_signing_signatory2) - Remove a signatory
* [update_signing_signatory2](#update_signing_signatory2) - Update a signatory

## create_signing_signatory2

Create a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="createSigningSignatory2" method="post" path="/signing/{connection_id}/signatory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.create_signing_signatory2(request={
        "signing_signatory": {},
        "connection_id": "<id>",
    })

    assert res.signing_signatory is not None

    # Handle response
    print(res.signing_signatory)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateSigningSignatory2Request](../../models/operations/createsigningsignatory2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateSigningSignatory2Response](../../models/operations/createsigningsignatory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_signing_signatory2

Retrieve a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="getSigningSignatory2" method="get" path="/signing/{connection_id}/signatory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.get_signing_signatory2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_signatory is not None

    # Handle response
    print(res.signing_signatory)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetSigningSignatory2Request](../../models/operations/getsigningsignatory2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetSigningSignatory2Response](../../models/operations/getsigningsignatory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_signing_signatories2

List all signatories

### Example Usage

<!-- UsageSnippet language="python" operationID="listSigningSignatories2" method="get" path="/signing/{connection_id}/signatory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.list_signing_signatories2(request={
        "connection_id": "<id>",
    })

    assert res.signing_signatories is not None

    # Handle response
    print(res.signing_signatories)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListSigningSignatories2Request](../../models/operations/listsigningsignatories2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListSigningSignatories2Response](../../models/operations/listsigningsignatories2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_signing_signatory2

Update a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="patchSigningSignatory2" method="patch" path="/signing/{connection_id}/signatory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.patch_signing_signatory2(request={
        "signing_signatory": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_signatory is not None

    # Handle response
    print(res.signing_signatory)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchSigningSignatory2Request](../../models/operations/patchsigningsignatory2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchSigningSignatory2Response](../../models/operations/patchsigningsignatory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_signing_signatory2

Remove a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="removeSigningSignatory2" method="delete" path="/signing/{connection_id}/signatory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.remove_signing_signatory2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveSigningSignatory2Request](../../models/operations/removesigningsignatory2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveSigningSignatory2Response](../../models/operations/removesigningsignatory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_signing_signatory2

Update a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSigningSignatory2" method="put" path="/signing/{connection_id}/signatory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.update_signing_signatory2(request={
        "signing_signatory": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_signatory is not None

    # Handle response
    print(res.signing_signatory)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateSigningSignatory2Request](../../models/operations/updatesigningsignatory2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateSigningSignatory2Response](../../models/operations/updatesigningsignatory2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |