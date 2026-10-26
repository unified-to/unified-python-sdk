# Domain

## Overview

### Available Operations

* [create_compute_domain](#create_compute_domain) - Create a domain
* [get_compute_domain](#get_compute_domain) - Retrieve a domain
* [list_compute_domains](#list_compute_domains) - List all domains
* [patch_compute_domain](#patch_compute_domain) - Update a domain
* [remove_compute_domain](#remove_compute_domain) - Remove a domain
* [update_compute_domain](#update_compute_domain) - Update a domain

## create_compute_domain

Creates a ComputeDomain. Provide the unified ComputeDomain fields in the request body; they are mapped to the provider's API. Returns the created ComputeDomain.

### Example Usage

<!-- UsageSnippet language="python" operationID="createComputeDomain" method="post" path="/compute/{connection_id}/domain" example="compute_domain" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.domain.create_compute_domain(request={
        "compute_domain": {
            "created_at": parse_datetime("2019-11-22T16:38:26.009Z"),
            "id": "c29172d4-7d18-4182-bb0a-ff51a49cd26d",
            "is_primary": False,
            "metadata": [],
            "name": "mysterious-republican.usable-section.info",
            "status": shared.ComputeDomainStatus.PENDING,
            "updated_at": parse_datetime("2023-11-06T12:11:06.940Z"),
        },
        "connection_id": "<id>",
    })

    assert res.compute_domain is not None

    # Handle response
    print(res.compute_domain)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateComputeDomainRequest](../../models/operations/createcomputedomainrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateComputeDomainResponse](../../models/operations/createcomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compute_domain

Retrieves a single ComputeDomain by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getComputeDomain" method="get" path="/compute/{connection_id}/domain/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.domain.get_compute_domain(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_domain is not None

    # Handle response
    print(res.compute_domain)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetComputeDomainRequest](../../models/operations/getcomputedomainrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetComputeDomainResponse](../../models/operations/getcomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compute_domains

Returns a list of ComputeDomains. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listComputeDomains" method="get" path="/compute/{connection_id}/domain" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.domain.list_compute_domains(request={
        "connection_id": "<id>",
    })

    assert res.compute_domains is not None

    # Handle response
    print(res.compute_domains)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListComputeDomainsRequest](../../models/operations/listcomputedomainsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListComputeDomainsResponse](../../models/operations/listcomputedomainsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_compute_domain

Updates the ComputeDomain identified by `id`. Provide the unified ComputeDomain fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchComputeDomain" method="patch" path="/compute/{connection_id}/domain/{id}" example="compute_domain" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.domain.patch_compute_domain(request={
        "compute_domain": {
            "created_at": parse_datetime("2019-11-22T16:38:26.009Z"),
            "id": "7ec2f710-0c0b-4365-a149-f60fbf38da23",
            "is_primary": False,
            "metadata": [],
            "name": "mysterious-republican.usable-section.info",
            "status": shared.ComputeDomainStatus.PENDING,
            "updated_at": parse_datetime("2023-11-06T12:11:06.947Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_domain is not None

    # Handle response
    print(res.compute_domain)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchComputeDomainRequest](../../models/operations/patchcomputedomainrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchComputeDomainResponse](../../models/operations/patchcomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_compute_domain

Deletes the ComputeDomain identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeComputeDomain" method="delete" path="/compute/{connection_id}/domain/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.domain.remove_compute_domain(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveComputeDomainRequest](../../models/operations/removecomputedomainrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveComputeDomainResponse](../../models/operations/removecomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_compute_domain

Updates the ComputeDomain identified by `id`. Provide the unified ComputeDomain fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateComputeDomain" method="put" path="/compute/{connection_id}/domain/{id}" example="compute_domain" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.domain.update_compute_domain(request={
        "compute_domain": {
            "created_at": parse_datetime("2019-11-22T16:38:26.009Z"),
            "id": "7ec2f710-0c0b-4365-a149-f60fbf38da23",
            "is_primary": False,
            "metadata": [],
            "name": "mysterious-republican.usable-section.info",
            "status": shared.ComputeDomainStatus.PENDING,
            "updated_at": parse_datetime("2023-11-06T12:11:06.947Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.compute_domain is not None

    # Handle response
    print(res.compute_domain)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateComputeDomainRequest](../../models/operations/updatecomputedomainrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateComputeDomainResponse](../../models/operations/updatecomputedomainresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |