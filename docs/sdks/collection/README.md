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
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCommerceCollectionRequest(
    connection_id='<value>',
)

res = s.collection.create_commerce_collection(req, operations.CreateCommerceCollectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateCommerceCollectionRequest](../../models/operations/createcommercecollectionrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.CreateCommerceCollectionSecurity](../../models/operations/createcommercecollectionsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCommerceCollectionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.collection.get_commerce_collection(req, operations.GetCommerceCollectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCommerceCollectionRequest](../../models/operations/getcommercecollectionrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetCommerceCollectionSecurity](../../models/operations/getcommercecollectionsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


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
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCommerceCollectionsRequest(
    connection_id='<value>',
)

res = s.collection.list_commerce_collections(req, operations.ListCommerceCollectionsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_collections is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListCommerceCollectionsRequest](../../models/operations/listcommercecollectionsrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ListCommerceCollectionsSecurity](../../models/operations/listcommercecollectionssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


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
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCommerceCollectionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.collection.patch_commerce_collection(req, operations.PatchCommerceCollectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PatchCommerceCollectionRequest](../../models/operations/patchcommercecollectionrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.PatchCommerceCollectionSecurity](../../models/operations/patchcommercecollectionsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


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
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCommerceCollectionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.collection.remove_commerce_collection(req, operations.RemoveCommerceCollectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.RemoveCommerceCollectionRequest](../../models/operations/removecommercecollectionrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.RemoveCommerceCollectionSecurity](../../models/operations/removecommercecollectionsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


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
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCommerceCollectionRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.collection.update_commerce_collection(req, operations.UpdateCommerceCollectionSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_collection is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdateCommerceCollectionRequest](../../models/operations/updatecommercecollectionrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.UpdateCommerceCollectionSecurity](../../models/operations/updatecommercecollectionsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.UpdateCommerceCollectionResponse](../../models/operations/updatecommercecollectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
