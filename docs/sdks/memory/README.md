# Memory

## Overview

### Available Operations

* [create_genai_memory](#create_genai_memory) - Create a memory
* [get_genai_memory](#get_genai_memory) - Retrieve a memory
* [list_genai_memories](#list_genai_memories) - List all memories
* [patch_genai_memory](#patch_genai_memory) - Update a memory
* [remove_genai_memory](#remove_genai_memory) - Remove a memory
* [update_genai_memory](#update_genai_memory) - Update a memory

## create_genai_memory

Creates a GenaiMemory. Provide the unified GenaiMemory fields in the request body; they are mapped to the provider's API. Returns the created GenaiMemory.

### Example Usage

<!-- UsageSnippet language="python" operationID="createGenaiMemory" method="post" path="/genai/{connection_id}/memory" example="genai_memory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.memory.create_genai_memory(request={
        "genai_memory": {
            "content": "Spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "00847e58-c148-4653-ac01-98cf4f0c0548",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "6d1774f7-a8ad-462d-9ba0-ece333056a26",
                    "namespace": "memory",
                    "slug": "defleo",
                    "value": "suffragium",
                },
            ],
            "name": "tabella.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-05-07T08:49:26.622Z"),
            "user_identifier": "70613433-847d-4db6-a8ea-96a2d7513dad",
        },
        "connection_id": "<id>",
    })

    assert res.genai_memory is not None

    # Handle response
    print(res.genai_memory)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateGenaiMemoryRequest](../../models/operations/creategenaimemoryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreateGenaiMemoryResponse](../../models/operations/creategenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_genai_memory

Retrieves a single GenaiMemory by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGenaiMemory" method="get" path="/genai/{connection_id}/memory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.memory.get_genai_memory(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_memory is not None

    # Handle response
    print(res.genai_memory)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetGenaiMemoryRequest](../../models/operations/getgenaimemoryrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetGenaiMemoryResponse](../../models/operations/getgenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_genai_memories

Returns a list of GenaiMemories. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listGenaiMemories" method="get" path="/genai/{connection_id}/memory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.memory.list_genai_memories(request={
        "connection_id": "<id>",
    })

    assert res.genai_memories is not None

    # Handle response
    print(res.genai_memories)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListGenaiMemoriesRequest](../../models/operations/listgenaimemoriesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListGenaiMemoriesResponse](../../models/operations/listgenaimemoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_genai_memory

Updates the GenaiMemory identified by `id`. Provide the unified GenaiMemory fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchGenaiMemory" method="patch" path="/genai/{connection_id}/memory/{id}" example="genai_memory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.memory.patch_genai_memory(request={
        "genai_memory": {
            "content": "Spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "5692cb03-46a7-4678-a28d-7f60bc5df5f5",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "6d1774f7-a8ad-462d-9ba0-ece333056a26",
                    "namespace": "memory",
                    "slug": "defleo",
                    "value": "suffragium",
                },
            ],
            "name": "tabella.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-05-07T08:49:26.626Z"),
            "user_identifier": "70613433-847d-4db6-a8ea-96a2d7513dad",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_memory is not None

    # Handle response
    print(res.genai_memory)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchGenaiMemoryRequest](../../models/operations/patchgenaimemoryrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.PatchGenaiMemoryResponse](../../models/operations/patchgenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_genai_memory

Deletes the GenaiMemory identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeGenaiMemory" method="delete" path="/genai/{connection_id}/memory/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.memory.remove_genai_memory(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveGenaiMemoryRequest](../../models/operations/removegenaimemoryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.RemoveGenaiMemoryResponse](../../models/operations/removegenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_genai_memory

Updates the GenaiMemory identified by `id`. Provide the unified GenaiMemory fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateGenaiMemory" method="put" path="/genai/{connection_id}/memory/{id}" example="genai_memory" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.memory.update_genai_memory(request={
        "genai_memory": {
            "content": "Spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "5692cb03-46a7-4678-a28d-7f60bc5df5f5",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "6d1774f7-a8ad-462d-9ba0-ece333056a26",
                    "namespace": "memory",
                    "slug": "defleo",
                    "value": "suffragium",
                },
            ],
            "name": "tabella.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-05-07T08:49:26.626Z"),
            "user_identifier": "70613433-847d-4db6-a8ea-96a2d7513dad",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.genai_memory is not None

    # Handle response
    print(res.genai_memory)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateGenaiMemoryRequest](../../models/operations/updategenaimemoryrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.UpdateGenaiMemoryResponse](../../models/operations/updategenaimemoryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |