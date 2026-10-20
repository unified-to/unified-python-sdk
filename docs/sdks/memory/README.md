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

Create a memory

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
            "content": "Tabella rem approbo spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis. Ullus ager degero deporto cicuta vulgivagus.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "038791ec-ae3e-4a95-b016-ae9d81752dda",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "7a8ad62d-ba0e-4ce3-8330-56a2647b5b3e",
                    "namespace": "memory",
                    "slug": "cribro",
                    "value": "aiunt",
                },
            ],
            "name": "sponte.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-04-25T12:41:10.266Z"),
            "user_identifier": "9d170613-4338-447d-bdb6-8ea96a2d7513",
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

Retrieve a memory

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

List all memories

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

Update a memory

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
            "content": "Tabella rem approbo spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis. Ullus ager degero deporto cicuta vulgivagus.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "1ee902dd-8a16-4215-91a6-541dbde221e6",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "7a8ad62d-ba0e-4ce3-8330-56a2647b5b3e",
                    "namespace": "memory",
                    "slug": "cribro",
                    "value": "aiunt",
                },
            ],
            "name": "sponte.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-04-25T12:41:10.270Z"),
            "user_identifier": "9d170613-4338-447d-bdb6-8ea96a2d7513",
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

Remove a memory

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

Update a memory

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
            "content": "Tabella rem approbo spiculum deserunt comitatus despecto. Aveho utroque accedo vinitor repellendus tam curis corona eos vobis. Ullus ager degero deporto cicuta vulgivagus.",
            "created_at": parse_datetime("2021-10-22T04:14:41.668Z"),
            "id": "1ee902dd-8a16-4215-91a6-541dbde221e6",
            "metadata": [
                {
                    "extra_data": {

                    },
                    "format_": shared.GenaiMetadataFormat.TEXT,
                    "id": "7a8ad62d-ba0e-4ce3-8330-56a2647b5b3e",
                    "namespace": "memory",
                    "slug": "cribro",
                    "value": "aiunt",
                },
            ],
            "name": "sponte.md",
            "type": shared.GenaiMemoryType.MEMORY,
            "updated_at": parse_datetime("2023-04-25T12:41:10.270Z"),
            "user_identifier": "9d170613-4338-447d-bdb6-8ea96a2d7513",
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