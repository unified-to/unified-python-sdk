# Passthrough

## Overview

### Available Operations

* [create_passthrough2_json](#create_passthrough2_json) - Passthrough POST
* [create_passthrough2_raw](#create_passthrough2_raw) - Passthrough POST
* [list_passthroughs2](#list_passthroughs2) - Passthrough GET
* [patch_passthrough2_json](#patch_passthrough2_json) - Passthrough PUT
* [patch_passthrough2_raw](#patch_passthrough2_raw) - Passthrough PUT
* [remove_passthrough2](#remove_passthrough2) - Passthrough DELETE
* [update_passthrough2_json](#update_passthrough2_json) - Passthrough PUT
* [update_passthrough2_raw](#update_passthrough2_raw) - Passthrough PUT

## create_passthrough2_json

Passthrough POST

### Example Usage

<!-- UsageSnippet language="python" operationID="createPassthrough2_json" method="post" path="/passthrough/{connection_id}/{path}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.create_passthrough2_json(request={
        "connection_id": "<id>",
        "path": "/net",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreatePassthrough2JSONRequest](../../models/operations/createpassthrough2jsonrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreatePassthrough2JSONResponse](../../models/operations/createpassthrough2jsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_passthrough2_raw

Passthrough POST

### Example Usage

<!-- UsageSnippet language="python" operationID="createPassthrough2_raw" method="post" path="/passthrough/{connection_id}/{path}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.create_passthrough2_raw(request={
        "connection_id": "<id>",
        "path": "/net",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreatePassthrough2RawRequest](../../models/operations/createpassthrough2rawrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreatePassthrough2RawResponse](../../models/operations/createpassthrough2rawresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_passthroughs2

Passthrough GET

### Example Usage

<!-- UsageSnippet language="python" operationID="listPassthroughs2" method="get" path="/passthrough/{connection_id}/{path}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.list_passthroughs2(request={
        "connection_id": "<id>",
        "path": "/usr/local/src",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListPassthroughs2Request](../../models/operations/listpassthroughs2request.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListPassthroughs2Response](../../models/operations/listpassthroughs2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_passthrough2_json

Passthrough PUT

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPassthrough2_json" method="patch" path="/passthrough/{connection_id}/{path}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.patch_passthrough2_json(request={
        "connection_id": "<id>",
        "path": "/usr/X11R6",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchPassthrough2JSONRequest](../../models/operations/patchpassthrough2jsonrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchPassthrough2JSONResponse](../../models/operations/patchpassthrough2jsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_passthrough2_raw

Passthrough PUT

### Example Usage

<!-- UsageSnippet language="python" operationID="patchPassthrough2_raw" method="patch" path="/passthrough/{connection_id}/{path}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.patch_passthrough2_raw(request={
        "connection_id": "<id>",
        "path": "/usr/X11R6",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchPassthrough2RawRequest](../../models/operations/patchpassthrough2rawrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchPassthrough2RawResponse](../../models/operations/patchpassthrough2rawresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_passthrough2

Passthrough DELETE

### Example Usage

<!-- UsageSnippet language="python" operationID="removePassthrough2" method="delete" path="/passthrough/{connection_id}/{path}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.remove_passthrough2(request={
        "connection_id": "<id>",
        "path": "/usr/include",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemovePassthrough2Request](../../models/operations/removepassthrough2request.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemovePassthrough2Response](../../models/operations/removepassthrough2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_passthrough2_json

Passthrough PUT

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePassthrough2_json" method="put" path="/passthrough/{connection_id}/{path}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.update_passthrough2_json(request={
        "connection_id": "<id>",
        "path": "/home/user/dir",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdatePassthrough2JSONRequest](../../models/operations/updatepassthrough2jsonrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdatePassthrough2JSONResponse](../../models/operations/updatepassthrough2jsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_passthrough2_raw

Passthrough PUT

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePassthrough2_raw" method="put" path="/passthrough/{connection_id}/{path}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.passthrough.update_passthrough2_raw(request={
        "connection_id": "<id>",
        "path": "/home/user/dir",
    })

    assert res.default_application_json_any is not None

    # Handle response
    print(res.default_application_json_any)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdatePassthrough2RawRequest](../../models/operations/updatepassthrough2rawrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdatePassthrough2RawResponse](../../models/operations/updatepassthrough2rawresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |