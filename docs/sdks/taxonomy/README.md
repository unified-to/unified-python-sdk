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
            "created_at": parse_datetime("2022-06-23T02:10:00.789Z"),
            "description": "Apto demonstro audacia adstringo cursim tristis solio careo.",
            "domain": "Electronics",
            "id": "ede085db-5709-4d53-a490-746f3de5be17",
            "is_active": False,
            "name": "International Functionality Architect",
            "parent_id": "6524b2a7-6520-4e15-8c4e-1aa6793db837",
            "role_ids": [
                "2b1ef757-eb4c-4207-8af1-929afe49cd65",
            ],
            "subcategory": "Bamboo",
            "type": shared.HrisTaxonomyType.KNOWLEDGE,
            "updated_at": parse_datetime("2023-05-22T04:57:25.374Z"),
            "url": "https://our-polarisation.name",
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