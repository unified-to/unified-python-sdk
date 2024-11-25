# Space
(*space*)

## Overview

### Available Operations

* [create_kms_space](#create_kms_space) - Create a space
* [get_kms_space](#get_kms_space) - Retrieve a space
* [list_kms_spaces](#list_kms_spaces) - List all spaces
* [patch_kms_space](#patch_kms_space) - Update a space
* [remove_kms_space](#remove_kms_space) - Remove a space
* [update_kms_space](#update_kms_space) - Update a space

## create_kms_space

Create a space

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.space.create_kms_space(request={
    "connection_id": "<value>",
})

if res.kms_space is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateKmsSpaceRequest](../../models/operations/createkmsspacerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.CreateKmsSpaceResponse](../../models/operations/createkmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_kms_space

Retrieve a space

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.space.get_kms_space(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.kms_space is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetKmsSpaceRequest](../../models/operations/getkmsspacerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetKmsSpaceResponse](../../models/operations/getkmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_kms_spaces

List all spaces

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.space.list_kms_spaces(request={
    "connection_id": "<value>",
})

if res.kms_spaces is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListKmsSpacesRequest](../../models/operations/listkmsspacesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.ListKmsSpacesResponse](../../models/operations/listkmsspacesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_kms_space

Update a space

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.space.patch_kms_space(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.kms_space is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PatchKmsSpaceRequest](../../models/operations/patchkmsspacerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.PatchKmsSpaceResponse](../../models/operations/patchkmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_kms_space

Remove a space

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.space.remove_kms_space(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RemoveKmsSpaceRequest](../../models/operations/removekmsspacerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.RemoveKmsSpaceResponse](../../models/operations/removekmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_kms_space

Update a space

### Example Usage

```python
from unified_python_sdk import UnifiedTo

s = UnifiedTo()

res = s.space.update_kms_space(request={
    "connection_id": "<value>",
    "id": "<id>",
})

if res.kms_space is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateKmsSpaceRequest](../../models/operations/updatekmsspacerequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.UpdateKmsSpaceResponse](../../models/operations/updatekmsspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |