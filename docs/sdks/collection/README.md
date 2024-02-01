# Collection
(*collection*)

### Available Operations

* [create_commerce_collection](#create_commerce_collection) - Create a collection
* [get_commerce_collection](#get_commerce_collection) - Retrieve a collection
* [list_commerce_collections](#list_commerce_collections) - List all collections
* [patch_commerce_collection](#patch_commerce_collection) - Update a collection
* [remove_commerce_collection](#remove_commerce_collection) - Remove a collection
* [update_commerce_collection](#update_commerce_collection) - Update a collection

## create_commerce_collection

Create a collection

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateCommerceCollectionRequest(
    commerce_collection=shared.CommerceCollection(
        id='<ID>',
        item_ids=[
            'string',
        ],
        media=[
            shared.CommerceItemMedia(
                url='http://uneven-mattress.name',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
    ),
    connection_id='string',
)

res = s.collection.create_commerce_collection(req)

if res.commerce_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateCommerceCollectionRequest](../../models/operations/createcommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.CreateCommerceCollectionResponse](../../models/operations/createcommercecollectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_commerce_collection

Retrieve a collection

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetCommerceCollectionRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.collection.get_commerce_collection(req)

if res.commerce_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCommerceCollectionRequest](../../models/operations/getcommercecollectionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetCommerceCollectionResponse](../../models/operations/getcommercecollectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_commerce_collections

List all collections

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListCommerceCollectionsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.collection.list_commerce_collections(req)

if res.commerce_collections is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListCommerceCollectionsRequest](../../models/operations/listcommercecollectionsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ListCommerceCollectionsResponse](../../models/operations/listcommercecollectionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_commerce_collection

Update a collection

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PatchCommerceCollectionRequest(
    commerce_collection=shared.CommerceCollection(
        id='<ID>',
        item_ids=[
            'string',
        ],
        media=[
            shared.CommerceItemMedia(
                url='http://personal-sorrow.com',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.collection.patch_commerce_collection(req)

if res.commerce_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchCommerceCollectionRequest](../../models/operations/patchcommercecollectionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PatchCommerceCollectionResponse](../../models/operations/patchcommercecollectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_commerce_collection

Remove a collection

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveCommerceCollectionRequest(
    connection_id='string',
    id='<ID>',
)

res = s.collection.remove_commerce_collection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveCommerceCollectionRequest](../../models/operations/removecommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.RemoveCommerceCollectionResponse](../../models/operations/removecommercecollectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_commerce_collection

Update a collection

### Example Usage

```python
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.UpdateCommerceCollectionRequest(
    commerce_collection=shared.CommerceCollection(
        id='<ID>',
        item_ids=[
            'string',
        ],
        media=[
            shared.CommerceItemMedia(
                url='https://stupid-entity.org',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.collection.update_commerce_collection(req)

if res.commerce_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateCommerceCollectionRequest](../../models/operations/updatecommercecollectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.UpdateCommerceCollectionResponse](../../models/operations/updatecommercecollectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
