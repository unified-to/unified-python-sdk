# Metadata
(*metadata*)

## Overview

### Available Operations

* [create_commerce_metadata](#create_commerce_metadata) - Create a metadata
* [get_commerce_metadata](#get_commerce_metadata) - Retrieve a metadata
* [list_commerce_metadatas](#list_commerce_metadatas) - List all metadatas
* [patch_commerce_metadata](#patch_commerce_metadata) - Update a metadata
* [remove_commerce_metadata](#remove_commerce_metadata) - Remove a metadata
* [update_commerce_metadata](#update_commerce_metadata) - Update a metadata

## create_commerce_metadata

Create a metadata

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.metadata.create_commerce_metadata(request=operations.CreateCommerceMetadataRequest(
    connection_id='<id>',
))

if res.commerce_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateCommerceMetadataRequest](../../models/operations/createcommercemetadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |

### Response

**[operations.CreateCommerceMetadataResponse](../../models/operations/createcommercemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_metadata

Retrieve a metadata

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.metadata.get_commerce_metadata(request=operations.GetCommerceMetadataRequest(
    connection_id='<id>',
    id='<id>',
))

if res.commerce_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetCommerceMetadataRequest](../../models/operations/getcommercemetadatarequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |

### Response

**[operations.GetCommerceMetadataResponse](../../models/operations/getcommercemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_metadatas

List all metadatas

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.metadata.list_commerce_metadatas(request=operations.ListCommerceMetadatasRequest(
    connection_id='<id>',
))

if res.commerce_metadatas is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListCommerceMetadatasRequest](../../models/operations/listcommercemetadatasrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |

### Response

**[operations.ListCommerceMetadatasResponse](../../models/operations/listcommercemetadatasresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_metadata

Update a metadata

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.metadata.patch_commerce_metadata(request=operations.PatchCommerceMetadataRequest(
    connection_id='<id>',
    id='<id>',
))

if res.commerce_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchCommerceMetadataRequest](../../models/operations/patchcommercemetadatarequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |

### Response

**[operations.PatchCommerceMetadataResponse](../../models/operations/patchcommercemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_metadata

Remove a metadata

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.metadata.remove_commerce_metadata(request=operations.RemoveCommerceMetadataRequest(
    connection_id='<id>',
    id='<id>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveCommerceMetadataRequest](../../models/operations/removecommercemetadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |

### Response

**[operations.RemoveCommerceMetadataResponse](../../models/operations/removecommercemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_metadata

Update a metadata

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.metadata.update_commerce_metadata(request=operations.UpdateCommerceMetadataRequest(
    connection_id='<id>',
    id='<id>',
))

if res.commerce_metadata is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateCommerceMetadataRequest](../../models/operations/updatecommercemetadatarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |

### Response

**[operations.UpdateCommerceMetadataResponse](../../models/operations/updatecommercemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |