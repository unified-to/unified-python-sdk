# Collection

## Overview

### Available Operations

* [create_commerce_collection](#create_commerce_collection) - Create a collection
* [create_lms_collection](#create_lms_collection) - Create a collection
* [get_commerce_collection](#get_commerce_collection) - Retrieve a collection
* [get_lms_collection](#get_lms_collection) - Retrieve a collection
* [list_commerce_collections](#list_commerce_collections) - List all collections
* [list_lms_collections](#list_lms_collections) - List all collections
* [patch_commerce_collection](#patch_commerce_collection) - Update a collection
* [patch_lms_collection](#patch_lms_collection) - Update a collection
* [remove_commerce_collection](#remove_commerce_collection) - Remove a collection
* [remove_lms_collection](#remove_lms_collection) - Remove a collection
* [update_commerce_collection](#update_commerce_collection) - Update a collection
* [update_lms_collection](#update_lms_collection) - Update a collection

## create_commerce_collection

Create a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="createCommerceCollection" method="post" path="/commerce/{connection_id}/collection" example="commerce_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.create_commerce_collection(request={
        "commerce_collection": {
            "created_at": parse_datetime("2023-07-14T00:42:54.742Z"),
            "description": "The Integrated leading edge website Cheese offers reliable performance and productive design",
            "id": "6cbdfe6c-1797-4bc8-8c24-8795b19ec5df",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "4f8b2f19-3212-4ea4-b395-b5e9f028d42b",
                    "metadata": [
                        {
                            "id": "c5a8f2f7-26df-4426-8dad-d54c42169644",
                            "slug": "censura",
                            "value": "toties",
                        },
                    ],
                    "position": 80.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/1319/1257?lock=7280448425732025",
                    "width": 40.0,
                },
            ],
            "metadata": [
                {
                    "id": "45a0d542-5384-42f5-9dce-9866f7e58fe4",
                    "slug": "aetas",
                    "value": "consuasor",
                },
            ],
            "name": "Small Marble Chips",
            "public_description": "Generic Gloves designed with Cotton for miserable performance",
            "public_name": "Small Marble Chips",
            "tags": [
                "ambulo",
                "adeptio",
                "contego",
            ],
            "type": shared.CommerceCollectionType.COLLECTION,
            "updated_at": parse_datetime("2025-02-26T21:04:10.562Z"),
        },
        "connection_id": "<id>",
    })

    assert res.commerce_collection is not None

    # Handle response
    print(res.commerce_collection)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateCommerceCollectionRequest](../../models/operations/createcommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.CreateCommerceCollectionResponse](../../models/operations/createcommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_lms_collection

Create a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="createLmsCollection" method="post" path="/lms/{connection_id}/collection" example="lms_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.create_lms_collection(request={
        "lms_collection": {
            "created_at": parse_datetime("2019-08-19T14:40:29.227Z"),
            "description": "Ab.",
            "id": "c5e3264d-5ed9-4a44-9d53-3b126ec6ba9b",
            "is_active": True,
            "media": [
                {
                    "content": "Accusamus earum sulum libero adficio testimonium vitae. Calcar contra vergo curis sollers. Caste brevis denuo. Tam amita ducimus capillus. Vulgaris temporibus arbustum solium id. Suppono commodo fuga surculus tripudio doloribus.",
                    "description": "Aliquam tardus careo hic umbra.",
                    "languages": [
                        "gl",
                    ],
                    "name": "thymum",
                    "thumbnail_url": "https://picsum.photos/seed/15O5EfV/2982/752",
                    "type": shared.LmsMediaType.HEADSHOT,
                    "url": "https://loremflickr.com/2679/70?lock=6078357625960554",
                },
            ],
            "name": "ara",
            "updated_at": parse_datetime("2026-06-29T14:35:16.788Z"),
        },
        "connection_id": "<id>",
    })

    assert res.lms_collection is not None

    # Handle response
    print(res.lms_collection)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateLmsCollectionRequest](../../models/operations/createlmscollectionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.CreateLmsCollectionResponse](../../models/operations/createlmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_commerce_collection

Retrieve a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="getCommerceCollection" method="get" path="/commerce/{connection_id}/collection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.get_commerce_collection(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_collection is not None

    # Handle response
    print(res.commerce_collection)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCommerceCollectionRequest](../../models/operations/getcommercecollectionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.GetCommerceCollectionResponse](../../models/operations/getcommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_lms_collection

Retrieve a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="getLmsCollection" method="get" path="/lms/{connection_id}/collection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.get_lms_collection(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_collection is not None

    # Handle response
    print(res.lms_collection)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetLmsCollectionRequest](../../models/operations/getlmscollectionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetLmsCollectionResponse](../../models/operations/getlmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_commerce_collections

List all collections

### Example Usage

<!-- UsageSnippet language="python" operationID="listCommerceCollections" method="get" path="/commerce/{connection_id}/collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.list_commerce_collections(request={
        "connection_id": "<id>",
    })

    assert res.commerce_collections is not None

    # Handle response
    print(res.commerce_collections)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListCommerceCollectionsRequest](../../models/operations/listcommercecollectionsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ListCommerceCollectionsResponse](../../models/operations/listcommercecollectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_lms_collections

List all collections

### Example Usage

<!-- UsageSnippet language="python" operationID="listLmsCollections" method="get" path="/lms/{connection_id}/collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.list_lms_collections(request={
        "connection_id": "<id>",
    })

    assert res.lms_collections is not None

    # Handle response
    print(res.lms_collections)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListLmsCollectionsRequest](../../models/operations/listlmscollectionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListLmsCollectionsResponse](../../models/operations/listlmscollectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_commerce_collection

Update a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="patchCommerceCollection" method="patch" path="/commerce/{connection_id}/collection/{id}" example="commerce_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.patch_commerce_collection(request={
        "commerce_collection": {
            "created_at": parse_datetime("2023-07-14T00:42:54.742Z"),
            "description": "The Integrated leading edge website Cheese offers reliable performance and productive design",
            "id": "5f1ecca3-a058-4dec-8120-d749299799d5",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "c0434bd3-d738-4c57-a4be-2be315d17366",
                    "metadata": [
                        {
                            "id": "769f2e48-3d95-4c62-a7f6-db9fdbaa79ff",
                            "slug": "censura",
                            "value": "toties",
                        },
                    ],
                    "position": 80.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/1319/1257?lock=7280448425732025",
                    "width": 40.0,
                },
            ],
            "metadata": [
                {
                    "id": "da4948b4-1c0d-4ce2-827d-0fc29f216c45",
                    "slug": "aetas",
                    "value": "consuasor",
                },
            ],
            "name": "Small Marble Chips",
            "public_description": "Generic Gloves designed with Cotton for miserable performance",
            "public_name": "Small Marble Chips",
            "tags": [
                "ambulo",
                "adeptio",
                "contego",
            ],
            "type": shared.CommerceCollectionType.COLLECTION,
            "updated_at": parse_datetime("2025-02-26T21:04:10.574Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_collection is not None

    # Handle response
    print(res.commerce_collection)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchCommerceCollectionRequest](../../models/operations/patchcommercecollectionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.PatchCommerceCollectionResponse](../../models/operations/patchcommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_lms_collection

Update a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="patchLmsCollection" method="patch" path="/lms/{connection_id}/collection/{id}" example="lms_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.patch_lms_collection(request={
        "lms_collection": {
            "created_at": parse_datetime("2019-08-19T14:40:29.227Z"),
            "description": "Ab.",
            "id": "1e4ddb70-1d97-488c-8382-28ab11bf2b0d",
            "is_active": True,
            "media": [
                {
                    "content": "Accusamus earum sulum libero adficio testimonium vitae. Calcar contra vergo curis sollers. Caste brevis denuo. Tam amita ducimus capillus. Vulgaris temporibus arbustum solium id. Suppono commodo fuga surculus tripudio doloribus.",
                    "description": "Aliquam tardus careo hic umbra.",
                    "languages": [
                        "gl",
                    ],
                    "name": "thymum",
                    "thumbnail_url": "https://picsum.photos/seed/15O5EfV/2982/752",
                    "type": shared.LmsMediaType.HEADSHOT,
                    "url": "https://loremflickr.com/2679/70?lock=6078357625960554",
                },
            ],
            "name": "ara",
            "updated_at": parse_datetime("2026-06-29T14:35:16.795Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_collection is not None

    # Handle response
    print(res.lms_collection)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchLmsCollectionRequest](../../models/operations/patchlmscollectionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.PatchLmsCollectionResponse](../../models/operations/patchlmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_commerce_collection

Remove a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="removeCommerceCollection" method="delete" path="/commerce/{connection_id}/collection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.remove_commerce_collection(request={
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveCommerceCollectionRequest](../../models/operations/removecommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RemoveCommerceCollectionResponse](../../models/operations/removecommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_lms_collection

Remove a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="removeLmsCollection" method="delete" path="/lms/{connection_id}/collection/{id}" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.remove_lms_collection(request={
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
| `request`                                                                                      | [operations.RemoveLmsCollectionRequest](../../models/operations/removelmscollectionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.RemoveLmsCollectionResponse](../../models/operations/removelmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_commerce_collection

Update a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCommerceCollection" method="put" path="/commerce/{connection_id}/collection/{id}" example="commerce_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.update_commerce_collection(request={
        "commerce_collection": {
            "created_at": parse_datetime("2023-07-14T00:42:54.742Z"),
            "description": "The Integrated leading edge website Cheese offers reliable performance and productive design",
            "id": "5f1ecca3-a058-4dec-8120-d749299799d5",
            "is_active": True,
            "is_featured": False,
            "is_visible": False,
            "item_metadata": [],
            "media": [
                {
                    "alt": "Defungo adopto thorax.",
                    "height": 759.0,
                    "id": "c0434bd3-d738-4c57-a4be-2be315d17366",
                    "metadata": [
                        {
                            "id": "769f2e48-3d95-4c62-a7f6-db9fdbaa79ff",
                            "slug": "censura",
                            "value": "toties",
                        },
                    ],
                    "position": 80.0,
                    "type": shared.CommerceItemMediaType.VIDEO,
                    "url": "https://loremflickr.com/1319/1257?lock=7280448425732025",
                    "width": 40.0,
                },
            ],
            "metadata": [
                {
                    "id": "da4948b4-1c0d-4ce2-827d-0fc29f216c45",
                    "slug": "aetas",
                    "value": "consuasor",
                },
            ],
            "name": "Small Marble Chips",
            "public_description": "Generic Gloves designed with Cotton for miserable performance",
            "public_name": "Small Marble Chips",
            "tags": [
                "ambulo",
                "adeptio",
                "contego",
            ],
            "type": shared.CommerceCollectionType.COLLECTION,
            "updated_at": parse_datetime("2025-02-26T21:04:10.574Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.commerce_collection is not None

    # Handle response
    print(res.commerce_collection)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateCommerceCollectionRequest](../../models/operations/updatecommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.UpdateCommerceCollectionResponse](../../models/operations/updatecommercecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_lms_collection

Update a collection

### Example Usage

<!-- UsageSnippet language="python" operationID="updateLmsCollection" method="put" path="/lms/{connection_id}/collection/{id}" example="lms_collection" -->
```python
from unified_python_sdk import UnifiedTo
from unified_python_sdk.models import shared
from unified_python_sdk.utils import parse_datetime


with UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
) as unified_to:

    res = unified_to.collection.update_lms_collection(request={
        "lms_collection": {
            "created_at": parse_datetime("2019-08-19T14:40:29.227Z"),
            "description": "Ab.",
            "id": "1e4ddb70-1d97-488c-8382-28ab11bf2b0d",
            "is_active": True,
            "media": [
                {
                    "content": "Accusamus earum sulum libero adficio testimonium vitae. Calcar contra vergo curis sollers. Caste brevis denuo. Tam amita ducimus capillus. Vulgaris temporibus arbustum solium id. Suppono commodo fuga surculus tripudio doloribus.",
                    "description": "Aliquam tardus careo hic umbra.",
                    "languages": [
                        "gl",
                    ],
                    "name": "thymum",
                    "thumbnail_url": "https://picsum.photos/seed/15O5EfV/2982/752",
                    "type": shared.LmsMediaType.HEADSHOT,
                    "url": "https://loremflickr.com/2679/70?lock=6078357625960554",
                },
            ],
            "name": "ara",
            "updated_at": parse_datetime("2026-06-29T14:35:16.795Z"),
        },
        "connection_id": "<id>",
        "id": "<id>",
    })

    assert res.lms_collection is not None

    # Handle response
    print(res.lms_collection)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateLmsCollectionRequest](../../models/operations/updatelmscollectionrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UpdateLmsCollectionResponse](../../models/operations/updatelmscollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |