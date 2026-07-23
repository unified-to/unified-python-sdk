# Source

## Overview

### Available Operations

* [create_cdp_source](#create_cdp_source) - Create a source
* [get_cdp_source](#get_cdp_source) - Retrieve a source
* [list_cdp_sources](#list_cdp_sources) - List all sources
* [patch_cdp_source](#patch_cdp_source) - Update a source
* [remove_cdp_source](#remove_cdp_source) - Remove a source
* [update_cdp_source](#update_cdp_source) - Update a source

## create_cdp_source

Create a source

### Example Usage

<!-- UsageSnippet language="python" operationID="createCdpSource" method="post" path="/cdp/{connection_id}/source" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.source.create_cdp_source(request={
        "cdp_source": {},
        "connection_id": "<id>",
    })

    assert res.cdp_source is not None

    # Handle response
    print(res.cdp_source)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateCdpSourceRequest](../../models/operations/createcdpsourcerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateCdpSourceResponse](../../models/operations/createcdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_cdp_source

Retrieve a source

### Example Usage

<!-- UsageSnippet language="python" operationID="getCdpSource" method="get" path="/cdp/{connection_id}/source/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.source.get_cdp_source(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_source is not None

    # Handle response
    print(res.cdp_source)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetCdpSourceRequest](../../models/operations/getcdpsourcerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetCdpSourceResponse](../../models/operations/getcdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_cdp_sources

List all sources

### Example Usage

<!-- UsageSnippet language="python" operationID="listCdpSources" method="get" path="/cdp/{connection_id}/source" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.source.list_cdp_sources(request={
        "connection_id": "<id>",
    })

    assert res.cdp_sources is not None

    # Handle response
    print(res.cdp_sources)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListCdpSourcesRequest](../../models/operations/listcdpsourcesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.ListCdpSourcesResponse](../../models/operations/listcdpsourcesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_cdp_source

Update a source

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCdpSource" method="patch" path="/cdp/{connection_id}/source/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.source.patch_cdp_source(request={
        "cdp_source": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_source is not None

    # Handle response
    print(res.cdp_source)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PatchCdpSourceRequest](../../models/operations/patchcdpsourcerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.PatchCdpSourceResponse](../../models/operations/patchcdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_cdp_source

Remove a source

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCdpSource" method="delete" path="/cdp/{connection_id}/source/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.source.remove_cdp_source(request={
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
| `request`                                                                              | [operations.RemoveCdpSourceRequest](../../models/operations/removecdpsourcerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.RemoveCdpSourceResponse](../../models/operations/removecdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_cdp_source

Update a source

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCdpSource" method="put" path="/cdp/{connection_id}/source/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.source.update_cdp_source(request={
        "cdp_source": {},
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.cdp_source is not None

    # Handle response
    print(res.cdp_source)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateCdpSourceRequest](../../models/operations/updatecdpsourcerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UpdateCdpSourceResponse](../../models/operations/updatecdpsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |