# Request

## Overview

### Available Operations

* [create_verification_request2](#create_verification_request2) - Create a request
* [get_verification_request2](#get_verification_request2) - Retrieve a request
* [list_verification_requests2](#list_verification_requests2) - List all requests
* [patch_verification_request2](#patch_verification_request2) - Update a request
* [remove_verification_request2](#remove_verification_request2) - Remove a request
* [update_verification_request2](#update_verification_request2) - Update a request

## create_verification_request2

Create a request

### Example Usage

<!-- UsageSnippet language="python" operationID="createVerificationRequest2" method="post" path="/verification/{connection_id}/request" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.request.create_verification_request2(request={
        "verification_request": {},
        "connection_id": "<id>",
    })

    assert res.verification_request is not None

    # Handle response
    print(res.verification_request)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateVerificationRequest2Request](../../models/operations/createverificationrequest2request.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.CreateVerificationRequest2Response](../../models/operations/createverificationrequest2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_verification_request2

Retrieve a request

### Example Usage

<!-- UsageSnippet language="python" operationID="getVerificationRequest2" method="get" path="/verification/{connection_id}/request/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.request.get_verification_request2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.verification_request is not None

    # Handle response
    print(res.verification_request)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetVerificationRequest2Request](../../models/operations/getverificationrequest2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GetVerificationRequest2Response](../../models/operations/getverificationrequest2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_verification_requests2

List all requests

### Example Usage

<!-- UsageSnippet language="python" operationID="listVerificationRequests2" method="get" path="/verification/{connection_id}/request" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.request.list_verification_requests2(request={
        "connection_id": "<id>",
    })

    assert res.verification_requests is not None

    # Handle response
    print(res.verification_requests)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListVerificationRequests2Request](../../models/operations/listverificationrequests2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.ListVerificationRequests2Response](../../models/operations/listverificationrequests2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_verification_request2

Update a request

### Example Usage

<!-- UsageSnippet language="python" operationID="patchVerificationRequest2" method="patch" path="/verification/{connection_id}/request/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.request.patch_verification_request2(request={
        "verification_request": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.verification_request is not None

    # Handle response
    print(res.verification_request)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchVerificationRequest2Request](../../models/operations/patchverificationrequest2request.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.PatchVerificationRequest2Response](../../models/operations/patchverificationrequest2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_verification_request2

Remove a request

### Example Usage

<!-- UsageSnippet language="python" operationID="removeVerificationRequest2" method="delete" path="/verification/{connection_id}/request/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.request.remove_verification_request2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.RemoveVerificationRequest2Request](../../models/operations/removeverificationrequest2request.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.RemoveVerificationRequest2Response](../../models/operations/removeverificationrequest2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_verification_request2

Update a request

### Example Usage

<!-- UsageSnippet language="python" operationID="updateVerificationRequest2" method="put" path="/verification/{connection_id}/request/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.request.update_verification_request2(request={
        "verification_request": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.verification_request is not None

    # Handle response
    print(res.verification_request)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateVerificationRequest2Request](../../models/operations/updateverificationrequest2request.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.UpdateVerificationRequest2Response](../../models/operations/updateverificationrequest2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |