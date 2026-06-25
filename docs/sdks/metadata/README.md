# Metadata

## Overview

### Available Operations

* [create_metadata_metadata2](#create_metadata_metadata2) - Create a metadata
* [get_metadata_metadata2](#get_metadata_metadata2) - Retrieve a metadata
* [list_metadata_metadatas2](#list_metadata_metadatas2) - List all metadatas
* [patch_metadata_metadata2](#patch_metadata_metadata2) - Update a metadata
* [remove_metadata_metadata2](#remove_metadata_metadata2) - Remove a metadata
* [update_metadata_metadata2](#update_metadata_metadata2) - Update a metadata

## create_metadata_metadata2

Create a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="createMetadataMetadata2" method="post" path="/metadata/{connection_id}/metadata" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.create_metadata_metadata2(request={
        "metadata_metadata": {
            "name": "<value>",
            "object_type": "<value>",
        },
        "connection_id": "<id>",
    })

    assert res.metadata_metadata is not None

    # Handle response
    print(res.metadata_metadata)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateMetadataMetadata2Request](../../models/operations/createmetadatametadata2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateMetadataMetadata2Response](../../models/operations/createmetadatametadata2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_metadata_metadata2

Retrieve a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="getMetadataMetadata2" method="get" path="/metadata/{connection_id}/metadata/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.get_metadata_metadata2(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.metadata_metadata is not None

    # Handle response
    print(res.metadata_metadata)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetMetadataMetadata2Request](../../models/operations/getmetadatametadata2request.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetMetadataMetadata2Response](../../models/operations/getmetadatametadata2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_metadata_metadatas2

List all metadatas

### Example Usage

<!-- UsageSnippet language="python" operationID="listMetadataMetadatas2" method="get" path="/metadata/{connection_id}/metadata" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.list_metadata_metadatas2(request={
        "connection_id": "<id>",
    })

    assert res.metadata_metadatas is not None

    # Handle response
    print(res.metadata_metadatas)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListMetadataMetadatas2Request](../../models/operations/listmetadatametadatas2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.ListMetadataMetadatas2Response](../../models/operations/listmetadatametadatas2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_metadata_metadata2

Update a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMetadataMetadata2" method="patch" path="/metadata/{connection_id}/metadata/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.patch_metadata_metadata2(request={
        "metadata_metadata": {
            "name": "<value>",
            "object_type": "<value>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.metadata_metadata is not None

    # Handle response
    print(res.metadata_metadata)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchMetadataMetadata2Request](../../models/operations/patchmetadatametadata2request.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.PatchMetadataMetadata2Response](../../models/operations/patchmetadatametadata2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_metadata_metadata2

Remove a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMetadataMetadata2" method="delete" path="/metadata/{connection_id}/metadata/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.remove_metadata_metadata2(request={
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
| `request`                                                                                              | [operations.RemoveMetadataMetadata2Request](../../models/operations/removemetadatametadata2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.RemoveMetadataMetadata2Response](../../models/operations/removemetadatametadata2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_metadata_metadata2

Update a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMetadataMetadata2" method="put" path="/metadata/{connection_id}/metadata/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.update_metadata_metadata2(request={
        "metadata_metadata": {
            "name": "<value>",
            "object_type": "<value>",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.metadata_metadata is not None

    # Handle response
    print(res.metadata_metadata)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateMetadataMetadata2Request](../../models/operations/updatemetadatametadata2request.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateMetadataMetadata2Response](../../models/operations/updatemetadatametadata2response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |