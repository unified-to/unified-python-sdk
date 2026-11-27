# Taxonomy

## Overview

### Available Operations

* [create_hris_taxonomy](#create_hris_taxonomy) - Create a taxonomy
* [get_hris_taxonomy](#get_hris_taxonomy) - Retrieve a taxonomy
* [list_crm_taxonomies](#list_crm_taxonomies) - List all taxonomies
* [list_hris_taxonomies](#list_hris_taxonomies) - List all taxonomies
* [patch_hris_taxonomy](#patch_hris_taxonomy) - Update a taxonomy
* [remove_hris_taxonomy](#remove_hris_taxonomy) - Remove a taxonomy
* [update_hris_taxonomy](#update_hris_taxonomy) - Update a taxonomy

## create_hris_taxonomy

Creates a HrisTaxonomy. Provide the unified HrisTaxonomy fields in the request body; they are mapped to the provider's API. Returns the created HrisTaxonomy.

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTaxonomy" method="post" path="/hris/{connection_id}/taxonomy" example="hris_taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxonomy.create_hris_taxonomy(request={
        "hris_taxonomy": {
            "alternative_names": [
                "Supervisor",
                "Customer",
            ],
            "created_at": parse_datetime("2022-06-23T02:10:00.789Z"),
            "description": "Ea commodo turbo.",
            "domain": "Music",
            "id": "f6ccb06c-80ca-4bff-9871-3894279f7704",
            "is_active": False,
            "metadata": [],
            "name": "Chief Accountability Representative",
            "subcategory": "Granite",
            "type": shared.HrisTaxonomyType.KNOWLEDGE,
            "updated_at": parse_datetime("2023-06-06T06:41:14.531Z"),
            "url": "https://happy-go-lucky-devastation.com",
        },
        "connection_id": "<id>",
    })

    assert res.hris_taxonomy is not None

    # Handle response
    print(res.hris_taxonomy)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateHrisTaxonomyRequest](../../models/operations/createhristaxonomyrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.CreateHrisTaxonomyResponse](../../models/operations/createhristaxonomyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_hris_taxonomy

Retrieves a single HrisTaxonomy by its `id`. Obtain `id` values from the corresponding list endpoint. Use `fields` to return only the fields you need.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHrisTaxonomy" method="get" path="/hris/{connection_id}/taxonomy/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxonomy.get_hris_taxonomy(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_taxonomy is not None

    # Handle response
    print(res.hris_taxonomy)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisTaxonomyRequest](../../models/operations/gethristaxonomyrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetHrisTaxonomyResponse](../../models/operations/gethristaxonomyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_crm_taxonomies

Returns a list of CrmTaxonomies. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listCrmTaxonomies" method="get" path="/crm/{connection_id}/taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxonomy.list_crm_taxonomies(request={
        "connection_id": "<id>",
    })

    assert res.crm_taxonomies is not None

    # Handle response
    print(res.crm_taxonomies)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCrmTaxonomiesRequest](../../models/operations/listcrmtaxonomiesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.ListCrmTaxonomiesResponse](../../models/operations/listcrmtaxonomiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_hris_taxonomies

Returns a list of HrisTaxonomies. Narrow the results with the query parameters before paging, then page through them with `limit` and `offset` (the default and maximum page size depend on the integration). Use `fields` to return only the fields you need and reduce the response size. When the integration supports a total count, it is returned in the `X-Total-Count` response header. Use each item's `id` to retrieve, update, or delete it where those operations are supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="listHrisTaxonomies" method="get" path="/hris/{connection_id}/taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxonomy.list_hris_taxonomies(request={
        "connection_id": "<id>",
    })

    assert res.hris_taxonomies is not None

    # Handle response
    print(res.hris_taxonomies)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListHrisTaxonomiesRequest](../../models/operations/listhristaxonomiesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListHrisTaxonomiesResponse](../../models/operations/listhristaxonomiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_hris_taxonomy

Updates the HrisTaxonomy identified by `id`. Provide the unified HrisTaxonomy fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="patchHrisTaxonomy" method="patch" path="/hris/{connection_id}/taxonomy/{id}" example="hris_taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxonomy.patch_hris_taxonomy(request={
        "hris_taxonomy": {
            "alternative_names": [
                "Supervisor",
                "Customer",
            ],
            "created_at": parse_datetime("2022-06-23T02:10:00.789Z"),
            "description": "Ea commodo turbo.",
            "domain": "Music",
            "id": "bdcb040f-aeac-425b-825b-4d026358aae2",
            "is_active": False,
            "metadata": [],
            "name": "Chief Accountability Representative",
            "subcategory": "Granite",
            "type": shared.HrisTaxonomyType.KNOWLEDGE,
            "updated_at": parse_datetime("2023-06-06T06:41:14.534Z"),
            "url": "https://happy-go-lucky-devastation.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_taxonomy is not None

    # Handle response
    print(res.hris_taxonomy)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchHrisTaxonomyRequest](../../models/operations/patchhristaxonomyrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PatchHrisTaxonomyResponse](../../models/operations/patchhristaxonomyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_hris_taxonomy

Deletes the HrisTaxonomy identified by `id`.

### Example Usage

<!-- UsageSnippet language="python" operationID="removeHrisTaxonomy" method="delete" path="/hris/{connection_id}/taxonomy/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxonomy.remove_hris_taxonomy(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveHrisTaxonomyRequest](../../models/operations/removehristaxonomyrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.RemoveHrisTaxonomyResponse](../../models/operations/removehristaxonomyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_hris_taxonomy

Updates the HrisTaxonomy identified by `id`. Provide the unified HrisTaxonomy fields to change in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateHrisTaxonomy" method="put" path="/hris/{connection_id}/taxonomy/{id}" example="hris_taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxonomy.update_hris_taxonomy(request={
        "hris_taxonomy": {
            "alternative_names": [
                "Supervisor",
                "Customer",
            ],
            "created_at": parse_datetime("2022-06-23T02:10:00.789Z"),
            "description": "Ea commodo turbo.",
            "domain": "Music",
            "id": "bdcb040f-aeac-425b-825b-4d026358aae2",
            "is_active": False,
            "metadata": [],
            "name": "Chief Accountability Representative",
            "subcategory": "Granite",
            "type": shared.HrisTaxonomyType.KNOWLEDGE,
            "updated_at": parse_datetime("2023-06-06T06:41:14.534Z"),
            "url": "https://happy-go-lucky-devastation.com",
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.hris_taxonomy is not None

    # Handle response
    print(res.hris_taxonomy)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateHrisTaxonomyRequest](../../models/operations/updatehristaxonomyrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.UpdateHrisTaxonomyResponse](../../models/operations/updatehristaxonomyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |