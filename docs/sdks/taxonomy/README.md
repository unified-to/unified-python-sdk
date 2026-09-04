# Taxonomy

## Overview

### Available Operations

* [create_hris_taxonomy](#create_hris_taxonomy) - Create a taxonomy
* [get_hris_taxonomy](#get_hris_taxonomy) - Retrieve a taxonomy
* [list_crm_taxonomies](#list_crm_taxonomies) - List all taxonomies
* [list_hris_taxonomies](#list_hris_taxonomies) - List all taxonomies

## create_hris_taxonomy

Create a taxonomy

### Example Usage

<!-- UsageSnippet language="python" operationID="createHrisTaxonomy" method="post" path="/hris/{connection_id}/taxonomy" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.taxonomy.create_hris_taxonomy(request={
        "hris_taxonomy": {},
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

Retrieve a taxonomy

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

List all taxonomies

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

List all taxonomies

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