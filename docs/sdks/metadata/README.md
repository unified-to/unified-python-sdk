# Metadata

## Overview

### Available Operations

* [create_metadata_metadata](#create_metadata_metadata) - Create a metadata
* [get_metadata_metadata](#get_metadata_metadata) - Retrieve a metadata
* [list_metadata_metadatas](#list_metadata_metadatas) - List all metadatas
* [patch_metadata_metadata](#patch_metadata_metadata) - Update a metadata
* [remove_metadata_metadata](#remove_metadata_metadata) - Remove a metadata
* [update_metadata_metadata](#update_metadata_metadata) - Update a metadata

## create_metadata_metadata

Create a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="createMetadataMetadata" method="post" path="/metadata/{connection_id}/metadata" example="metadata_metadata" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.create_metadata_metadata(request={
        "metadata_metadata": {
            "created_at": parse_datetime("2021-03-25T03:02:17.656Z"),
            "format_": shared.MetadataMetadataFormat.PRICE,
            "id": "6d18d563-91f9-409e-880d-ae0b124eaebc",
            "is_required": False,
            "name": "autem",
            "object_type": "clubs_group",
            "objects": {

            },
            "options": [],
            "original_format": "advoco",
            "slug": "arbustum",
            "updated_at": parse_datetime("2025-02-27T00:01:10.758Z"),
        },
        "connection_id": "<id>",
    })

    assert res.metadata_metadata is not None

    # Handle response
    print(res.metadata_metadata)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateMetadataMetadataRequest](../../models/operations/createmetadatametadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateMetadataMetadataResponse](../../models/operations/createmetadatametadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_metadata_metadata

Retrieve a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="getMetadataMetadata" method="get" path="/metadata/{connection_id}/metadata/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.get_metadata_metadata(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.metadata_metadata is not None

    # Handle response
    print(res.metadata_metadata)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetMetadataMetadataRequest](../../models/operations/getmetadatametadatarequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetMetadataMetadataResponse](../../models/operations/getmetadatametadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_metadata_metadatas

List all metadatas

### Example Usage

<!-- UsageSnippet language="python" operationID="listMetadataMetadatas" method="get" path="/metadata/{connection_id}/metadata" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.list_metadata_metadatas(request={
        "connection_id": "<id>",
    })

    assert res.metadata_metadatas is not None

    # Handle response
    print(res.metadata_metadatas)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListMetadataMetadatasRequest](../../models/operations/listmetadatametadatasrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.ListMetadataMetadatasResponse](../../models/operations/listmetadatametadatasresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_metadata_metadata

Update a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="patchMetadataMetadata" method="patch" path="/metadata/{connection_id}/metadata/{id}" example="metadata_metadata" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.patch_metadata_metadata(request={
        "metadata_metadata": {
            "created_at": parse_datetime("2021-03-25T03:02:17.656Z"),
            "format_": shared.MetadataMetadataFormat.PRICE,
            "id": "344c6ce6-59ef-45aa-92c2-bc0eb5bdc792",
            "is_required": False,
            "name": "autem",
            "object_type": "clubs_group",
            "objects": {

            },
            "options": [],
            "original_format": "advoco",
            "slug": "arbustum",
            "updated_at": parse_datetime("2025-02-27T00:01:10.764Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.metadata_metadata is not None

    # Handle response
    print(res.metadata_metadata)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchMetadataMetadataRequest](../../models/operations/patchmetadatametadatarequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PatchMetadataMetadataResponse](../../models/operations/patchmetadatametadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_metadata_metadata

Remove a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="removeMetadataMetadata" method="delete" path="/metadata/{connection_id}/metadata/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.remove_metadata_metadata(request={
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
| `request`                                                                                            | [operations.RemoveMetadataMetadataRequest](../../models/operations/removemetadatametadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RemoveMetadataMetadataResponse](../../models/operations/removemetadatametadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_metadata_metadata

Update a metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="updateMetadataMetadata" method="put" path="/metadata/{connection_id}/metadata/{id}" example="metadata_metadata" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.metadata.update_metadata_metadata(request={
        "metadata_metadata": {
            "created_at": parse_datetime("2021-03-25T03:02:17.656Z"),
            "format_": shared.MetadataMetadataFormat.PRICE,
            "id": "344c6ce6-59ef-45aa-92c2-bc0eb5bdc792",
            "is_required": False,
            "name": "autem",
            "object_type": "clubs_group",
            "objects": {

            },
            "options": [],
            "original_format": "advoco",
            "slug": "arbustum",
            "updated_at": parse_datetime("2025-02-27T00:01:10.764Z"),
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
| `request`                                                                                            | [operations.UpdateMetadataMetadataRequest](../../models/operations/updatemetadatametadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateMetadataMetadataResponse](../../models/operations/updatemetadatametadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |