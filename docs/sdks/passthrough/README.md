# Passthrough
(*passthrough*)

## Overview

### Available Operations

* [create_passthrough_json](#create_passthrough_json) - Passthrough POST
* [create_passthrough_raw](#create_passthrough_raw) - Passthrough POST
* [list_passthroughs](#list_passthroughs) - Passthrough GET
* [patch_passthrough_json](#patch_passthrough_json) - Passthrough PUT
* [patch_passthrough_raw](#patch_passthrough_raw) - Passthrough PUT
* [remove_passthrough](#remove_passthrough) - Passthrough DELETE
* [update_passthrough_json](#update_passthrough_json) - Passthrough PUT
* [update_passthrough_raw](#update_passthrough_raw) - Passthrough PUT

## create_passthrough_json

Passthrough POST

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.passthrough.create_passthrough_json(request=operations.CreatePassthroughJSONRequest(
    connection_id='<value>',
    path='/etc/periodic',
))

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreatePassthroughJSONRequest](../../models/operations/createpassthroughjsonrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |

### Response

**[operations.CreatePassthroughJSONResponse](../../models/operations/createpassthroughjsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_passthrough_raw

Passthrough POST

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.passthrough.create_passthrough_raw(request=operations.CreatePassthroughRawRequest(
    connection_id='<value>',
    path='/etc/periodic',
))

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreatePassthroughRawRequest](../../models/operations/createpassthroughrawrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |

### Response

**[operations.CreatePassthroughRawResponse](../../models/operations/createpassthroughrawresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_passthroughs

Passthrough GET

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.passthrough.list_passthroughs(request=operations.ListPassthroughsRequest(
    connection_id='<value>',
    path='/selinux',
))

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListPassthroughsRequest](../../models/operations/listpassthroughsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |

### Response

**[operations.ListPassthroughsResponse](../../models/operations/listpassthroughsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_passthrough_json

Passthrough PUT

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.passthrough.patch_passthrough_json(request=operations.PatchPassthroughJSONRequest(
    connection_id='<value>',
    path='/mnt',
))

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchPassthroughJSONRequest](../../models/operations/patchpassthroughjsonrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |

### Response

**[operations.PatchPassthroughJSONResponse](../../models/operations/patchpassthroughjsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_passthrough_raw

Passthrough PUT

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.passthrough.patch_passthrough_raw(request=operations.PatchPassthroughRawRequest(
    connection_id='<value>',
    path='/mnt',
))

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PatchPassthroughRawRequest](../../models/operations/patchpassthroughrawrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |

### Response

**[operations.PatchPassthroughRawResponse](../../models/operations/patchpassthroughrawresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_passthrough

Passthrough DELETE

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.passthrough.remove_passthrough(request=operations.RemovePassthroughRequest(
    connection_id='<value>',
    path='/Applications',
))

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemovePassthroughRequest](../../models/operations/removepassthroughrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |

### Response

**[operations.RemovePassthroughResponse](../../models/operations/removepassthroughresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_passthrough_json

Passthrough PUT

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.passthrough.update_passthrough_json(request=operations.UpdatePassthroughJSONRequest(
    connection_id='<value>',
    path='/dev',
))

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdatePassthroughJSONRequest](../../models/operations/updatepassthroughjsonrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |

### Response

**[operations.UpdatePassthroughJSONResponse](../../models/operations/updatepassthroughjsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_passthrough_raw

Passthrough PUT

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()


res = s.passthrough.update_passthrough_raw(request=operations.UpdatePassthroughRawRequest(
    connection_id='<value>',
    path='/dev',
))

if res.body is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdatePassthroughRawRequest](../../models/operations/updatepassthroughrawrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |

### Response

**[operations.UpdatePassthroughRawResponse](../../models/operations/updatepassthroughrawresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |