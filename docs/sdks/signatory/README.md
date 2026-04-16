# Signatory

## Overview

### Available Operations

* [create_signing_signatory](#create_signing_signatory) - Create a signatory
* [get_signing_signatory](#get_signing_signatory) - Retrieve a signatory
* [list_signing_signatories](#list_signing_signatories) - List all signatories
* [patch_signing_signatory](#patch_signing_signatory) - Update a signatory
* [remove_signing_signatory](#remove_signing_signatory) - Remove a signatory
* [update_signing_signatory](#update_signing_signatory) - Update a signatory

## create_signing_signatory

Create a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="createSigningSignatory" method="post" path="/signing/{connection_id}/signatory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.create_signing_signatory(request={
        "signing_signatory": {},
        "connection_id": "<id>",
    })

    assert res.signing_signatory is not None

    # Handle response
    print(res.signing_signatory)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateSigningSignatoryRequest](../../models/operations/createsigningsignatoryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateSigningSignatoryResponse](../../models/operations/createsigningsignatoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_signing_signatory

Retrieve a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="getSigningSignatory" method="get" path="/signing/{connection_id}/signatory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.get_signing_signatory(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_signatory is not None

    # Handle response
    print(res.signing_signatory)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetSigningSignatoryRequest](../../models/operations/getsigningsignatoryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetSigningSignatoryResponse](../../models/operations/getsigningsignatoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_signing_signatories

List all signatories

### Example Usage

<!-- UsageSnippet language="python" operationID="listSigningSignatories" method="get" path="/signing/{connection_id}/signatory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.list_signing_signatories(request={
        "connection_id": "<id>",
    })

    assert res.signing_signatories is not None

    # Handle response
    print(res.signing_signatories)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListSigningSignatoriesRequest](../../models/operations/listsigningsignatoriesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListSigningSignatoriesResponse](../../models/operations/listsigningsignatoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_signing_signatory

Update a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="patchSigningSignatory" method="patch" path="/signing/{connection_id}/signatory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.patch_signing_signatory(request={
        "signing_signatory": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_signatory is not None

    # Handle response
    print(res.signing_signatory)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchSigningSignatoryRequest](../../models/operations/patchsigningsignatoryrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchSigningSignatoryResponse](../../models/operations/patchsigningsignatoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_signing_signatory

Remove a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="removeSigningSignatory" method="delete" path="/signing/{connection_id}/signatory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.remove_signing_signatory(request={
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
| `request`                                                                                            | [operations.RemoveSigningSignatoryRequest](../../models/operations/removesigningsignatoryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveSigningSignatoryResponse](../../models/operations/removesigningsignatoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_signing_signatory

Update a signatory

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSigningSignatory" method="put" path="/signing/{connection_id}/signatory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.signatory.update_signing_signatory(request={
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
| `request`                                                                                            | [operations.UpdateSigningSignatoryRequest](../../models/operations/updatesigningsignatoryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateSigningSignatoryResponse](../../models/operations/updatesigningsignatoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |