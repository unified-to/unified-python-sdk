# Template

## Overview

### Available Operations

* [create_compute_template](#create_compute_template) - Create a template
* [get_compute_template](#get_compute_template) - Retrieve a template
* [get_signing_template](#get_signing_template) - Retrieve a template
* [list_compute_templates](#list_compute_templates) - List all templates
* [list_signing_templates](#list_signing_templates) - List all templates
* [patch_compute_template](#patch_compute_template) - Update a template
* [remove_compute_template](#remove_compute_template) - Remove a template
* [update_compute_template](#update_compute_template) - Update a template

## create_compute_template

Create a template

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeTemplate" method="post" path="/compute/{connection_id}/template" example="compute_template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.create_compute_template(request={
        "compute_template": {
            "cpu_count": 4.0,
            "created_at": parse_datetime("2023-02-23T03:28:59.864Z"),
            "disk_mb": 10240.0,
            "dockerfile": "FROM ubuntu:24.04\nRUN apt-get update",
            "gpu_count": 2.0,
            "gpu_model": shared.ComputeTemplateGpuModel.NVIDIA_GH200,
            "id": "82c60ba1-f300-47ad-85c3-4f3b54141341",
            "image": "perfumed-molasses/cohibeo:5.2",
            "is_public": False,
            "last_used_at": parse_datetime("2026-03-16T20:09:49.527Z"),
            "memory_mb": 8192.0,
            "metadata": [],
            "name": "multi-byte-card",
            "ports": [
                8080.0,
            ],
            "status": shared.ComputeTemplateStatus.OTHER,
            "updated_at": parse_datetime("2025-02-08T06:49:08.296Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_template is not None

    # Handle response
    print(res.compute_template)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateComputeTemplateRequest](../../models/operations/createcomputetemplaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.CreateComputeTemplateResponse](../../models/operations/createcomputetemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_template

Retrieve a template

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeTemplate" method="get" path="/compute/{connection_id}/template/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.get_compute_template(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_template is not None

    # Handle response
    print(res.compute_template)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetComputeTemplateRequest](../../models/operations/getcomputetemplaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetComputeTemplateResponse](../../models/operations/getcomputetemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_signing_template

Retrieve a template

### Example Usage

<!-- UsageSnippet language="python" operationID="getSigningTemplate" method="get" path="/signing/{connection_id}/template/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.get_signing_template(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.signing_template is not None

    # Handle response
    print(res.signing_template)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetSigningTemplateRequest](../../models/operations/getsigningtemplaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetSigningTemplateResponse](../../models/operations/getsigningtemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_templates

List all templates

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeTemplates" method="get" path="/compute/{connection_id}/template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.list_compute_templates(request={
        "connection_id": "<id>",
    })

    assert res.compute_templates is not None

    # Handle response
    print(res.compute_templates)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListComputeTemplatesRequest](../../models/operations/listcomputetemplatesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListComputeTemplatesResponse](../../models/operations/listcomputetemplatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_signing_templates

List all templates

### Example Usage

<!-- UsageSnippet language="python" operationID="listSigningTemplates" method="get" path="/signing/{connection_id}/template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.list_signing_templates(request={
        "connection_id": "<id>",
    })

    assert res.signing_templates is not None

    # Handle response
    print(res.signing_templates)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListSigningTemplatesRequest](../../models/operations/listsigningtemplatesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ListSigningTemplatesResponse](../../models/operations/listsigningtemplatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_template

Update a template

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeTemplate" method="patch" path="/compute/{connection_id}/template/{id}" example="compute_template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.patch_compute_template(request={
        "compute_template": {
            "cpu_count": 4.0,
            "created_at": parse_datetime("2023-02-23T03:28:59.864Z"),
            "disk_mb": 10240.0,
            "dockerfile": "FROM ubuntu:24.04\nRUN apt-get update",
            "gpu_count": 2.0,
            "gpu_model": shared.ComputeTemplateGpuModel.NVIDIA_GH200,
            "id": "dfeb7d78-728c-4dfd-a1ea-506c4faafa56",
            "image": "perfumed-molasses/cohibeo:5.2",
            "is_public": False,
            "last_used_at": parse_datetime("2026-03-16T20:09:49.547Z"),
            "memory_mb": 8192.0,
            "metadata": [],
            "name": "multi-byte-card",
            "ports": [
                8080.0,
            ],
            "status": shared.ComputeTemplateStatus.OTHER,
            "updated_at": parse_datetime("2025-02-08T06:49:08.309Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_template is not None

    # Handle response
    print(res.compute_template)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PatchComputeTemplateRequest](../../models/operations/patchcomputetemplaterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.PatchComputeTemplateResponse](../../models/operations/patchcomputetemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_template

Remove a template

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeTemplate" method="delete" path="/compute/{connection_id}/template/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.remove_compute_template(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveComputeTemplateRequest](../../models/operations/removecomputetemplaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.RemoveComputeTemplateResponse](../../models/operations/removecomputetemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_template

Update a template

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeTemplate" method="put" path="/compute/{connection_id}/template/{id}" example="compute_template" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.template.update_compute_template(request={
        "compute_template": {
            "cpu_count": 4.0,
            "created_at": parse_datetime("2023-02-23T03:28:59.864Z"),
            "disk_mb": 10240.0,
            "dockerfile": "FROM ubuntu:24.04\nRUN apt-get update",
            "gpu_count": 2.0,
            "gpu_model": shared.ComputeTemplateGpuModel.NVIDIA_GH200,
            "id": "dfeb7d78-728c-4dfd-a1ea-506c4faafa56",
            "image": "perfumed-molasses/cohibeo:5.2",
            "is_public": False,
            "last_used_at": parse_datetime("2026-03-16T20:09:49.547Z"),
            "memory_mb": 8192.0,
            "metadata": [],
            "name": "multi-byte-card",
            "ports": [
                8080.0,
            ],
            "status": shared.ComputeTemplateStatus.OTHER,
            "updated_at": parse_datetime("2025-02-08T06:49:08.309Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_template is not None

    # Handle response
    print(res.compute_template)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdateComputeTemplateRequest](../../models/operations/updatecomputetemplaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdateComputeTemplateResponse](../../models/operations/updatecomputetemplateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |