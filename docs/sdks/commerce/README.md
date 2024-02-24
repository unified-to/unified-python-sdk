# Commerce
(*commerce*)

### Available Operations

* [create_commerce_collection](#create_commerce_collection) - Create a collection
* [create_commerce_inventory](#create_commerce_inventory) - Create an inventory
* [create_commerce_item](#create_commerce_item) - Create an item
* [create_commerce_location](#create_commerce_location) - Create a location
* [get_commerce_collection](#get_commerce_collection) - Retrieve a collection
* [get_commerce_inventory](#get_commerce_inventory) - Retrieve an inventory
* [get_commerce_item](#get_commerce_item) - Retrieve an item
* [get_commerce_location](#get_commerce_location) - Retrieve a location
* [list_commerce_collections](#list_commerce_collections) - List all collections
* [list_commerce_inventories](#list_commerce_inventories) - List all inventories
* [list_commerce_items](#list_commerce_items) - List all items
* [list_commerce_locations](#list_commerce_locations) - List all locations
* [patch_commerce_collection](#patch_commerce_collection) - Update a collection
* [patch_commerce_inventory](#patch_commerce_inventory) - Update an inventory
* [patch_commerce_item](#patch_commerce_item) - Update an item
* [patch_commerce_location](#patch_commerce_location) - Update a location
* [remove_commerce_collection](#remove_commerce_collection) - Remove a collection
* [remove_commerce_inventory](#remove_commerce_inventory) - Remove an inventory
* [remove_commerce_item](#remove_commerce_item) - Remove an item
* [remove_commerce_location](#remove_commerce_location) - Remove a location
* [update_commerce_collection](#update_commerce_collection) - Update a collection
* [update_commerce_inventory](#update_commerce_inventory) - Update an inventory
* [update_commerce_item](#update_commerce_item) - Update an item
* [update_commerce_location](#update_commerce_location) - Update a location

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

res = s.commerce.create_commerce_collection(req, operations.CreateCommerceCollectionSecurity(
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

## create_commerce_inventory

Create an inventory

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCommerceInventoryRequest(
    connection_id='<value>',
)

res = s.commerce.create_commerce_inventory(req, operations.CreateCommerceInventorySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_inventory is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateCommerceInventoryRequest](../../models/operations/createcommerceinventoryrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.CreateCommerceInventorySecurity](../../models/operations/createcommerceinventorysecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.CreateCommerceInventoryResponse](../../models/operations/createcommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_commerce_item

Create an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCommerceItemRequest(
    connection_id='<value>',
)

res = s.commerce.create_commerce_item(req, operations.CreateCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateCommerceItemRequest](../../models/operations/createcommerceitemrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CreateCommerceItemSecurity](../../models/operations/createcommerceitemsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CreateCommerceItemResponse](../../models/operations/createcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_commerce_location

Create a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.CreateCommerceLocationRequest(
    connection_id='<value>',
)

res = s.commerce.create_commerce_location(req, operations.CreateCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateCommerceLocationRequest](../../models/operations/createcommercelocationrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.CreateCommerceLocationSecurity](../../models/operations/createcommercelocationsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.CreateCommerceLocationResponse](../../models/operations/createcommercelocationresponse.md)**
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

res = s.commerce.get_commerce_collection(req, operations.GetCommerceCollectionSecurity(
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

## get_commerce_inventory

Retrieve an inventory

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCommerceInventoryRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.get_commerce_inventory(req, operations.GetCommerceInventorySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_inventory is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCommerceInventoryRequest](../../models/operations/getcommerceinventoryrequest.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.GetCommerceInventorySecurity](../../models/operations/getcommerceinventorysecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.GetCommerceInventoryResponse](../../models/operations/getcommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_commerce_item

Retrieve an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCommerceItemRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.get_commerce_item(req, operations.GetCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCommerceItemRequest](../../models/operations/getcommerceitemrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetCommerceItemSecurity](../../models/operations/getcommerceitemsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetCommerceItemResponse](../../models/operations/getcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_commerce_location

Retrieve a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.GetCommerceLocationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.get_commerce_location(req, operations.GetCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCommerceLocationRequest](../../models/operations/getcommercelocationrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetCommerceLocationSecurity](../../models/operations/getcommercelocationsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetCommerceLocationResponse](../../models/operations/getcommercelocationresponse.md)**
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

res = s.commerce.list_commerce_collections(req, operations.ListCommerceCollectionsSecurity(
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

## list_commerce_inventories

List all inventories

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCommerceInventoriesRequest(
    connection_id='<value>',
)

res = s.commerce.list_commerce_inventories(req, operations.ListCommerceInventoriesSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_inventories is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListCommerceInventoriesRequest](../../models/operations/listcommerceinventoriesrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ListCommerceInventoriesSecurity](../../models/operations/listcommerceinventoriessecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.ListCommerceInventoriesResponse](../../models/operations/listcommerceinventoriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_commerce_items

List all items

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCommerceItemsRequest(
    connection_id='<value>',
)

res = s.commerce.list_commerce_items(req, operations.ListCommerceItemsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_items is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListCommerceItemsRequest](../../models/operations/listcommerceitemsrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListCommerceItemsSecurity](../../models/operations/listcommerceitemssecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListCommerceItemsResponse](../../models/operations/listcommerceitemsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_commerce_locations

List all locations

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.ListCommerceLocationsRequest(
    connection_id='<value>',
)

res = s.commerce.list_commerce_locations(req, operations.ListCommerceLocationsSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_locations is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListCommerceLocationsRequest](../../models/operations/listcommercelocationsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.ListCommerceLocationsSecurity](../../models/operations/listcommercelocationssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.ListCommerceLocationsResponse](../../models/operations/listcommercelocationsresponse.md)**
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

res = s.commerce.patch_commerce_collection(req, operations.PatchCommerceCollectionSecurity(
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

## patch_commerce_inventory

Update an inventory

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCommerceInventoryRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.patch_commerce_inventory(req, operations.PatchCommerceInventorySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_inventory is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PatchCommerceInventoryRequest](../../models/operations/patchcommerceinventoryrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.PatchCommerceInventorySecurity](../../models/operations/patchcommerceinventorysecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.PatchCommerceInventoryResponse](../../models/operations/patchcommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_commerce_item

Update an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCommerceItemRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.patch_commerce_item(req, operations.PatchCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PatchCommerceItemRequest](../../models/operations/patchcommerceitemrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.PatchCommerceItemSecurity](../../models/operations/patchcommerceitemsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.PatchCommerceItemResponse](../../models/operations/patchcommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_commerce_location

Update a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.PatchCommerceLocationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.patch_commerce_location(req, operations.PatchCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchCommerceLocationRequest](../../models/operations/patchcommercelocationrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PatchCommerceLocationSecurity](../../models/operations/patchcommercelocationsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PatchCommerceLocationResponse](../../models/operations/patchcommercelocationresponse.md)**
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

res = s.commerce.remove_commerce_collection(req, operations.RemoveCommerceCollectionSecurity(
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

## remove_commerce_inventory

Remove an inventory

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCommerceInventoryRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.remove_commerce_inventory(req, operations.RemoveCommerceInventorySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RemoveCommerceInventoryRequest](../../models/operations/removecommerceinventoryrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveCommerceInventorySecurity](../../models/operations/removecommerceinventorysecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveCommerceInventoryResponse](../../models/operations/removecommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_commerce_item

Remove an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCommerceItemRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.remove_commerce_item(req, operations.RemoveCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RemoveCommerceItemRequest](../../models/operations/removecommerceitemrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.RemoveCommerceItemSecurity](../../models/operations/removecommerceitemsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.RemoveCommerceItemResponse](../../models/operations/removecommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_commerce_location

Remove a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.RemoveCommerceLocationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.remove_commerce_location(req, operations.RemoveCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveCommerceLocationRequest](../../models/operations/removecommercelocationrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.RemoveCommerceLocationSecurity](../../models/operations/removecommercelocationsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.RemoveCommerceLocationResponse](../../models/operations/removecommercelocationresponse.md)**
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

res = s.commerce.update_commerce_collection(req, operations.UpdateCommerceCollectionSecurity(
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

## update_commerce_inventory

Update an inventory

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCommerceInventoryRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.update_commerce_inventory(req, operations.UpdateCommerceInventorySecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_inventory is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateCommerceInventoryRequest](../../models/operations/updatecommerceinventoryrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateCommerceInventorySecurity](../../models/operations/updatecommerceinventorysecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateCommerceInventoryResponse](../../models/operations/updatecommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_commerce_item

Update an item

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCommerceItemRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.update_commerce_item(req, operations.UpdateCommerceItemSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateCommerceItemRequest](../../models/operations/updatecommerceitemrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.UpdateCommerceItemSecurity](../../models/operations/updatecommerceitemsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.UpdateCommerceItemResponse](../../models/operations/updatecommerceitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_commerce_location

Update a location

### Example Usage

```python
import unified_to
from unified_to.models import operations

s = unified_to.UnifiedTo()

req = operations.UpdateCommerceLocationRequest(
    connection_id='<value>',
    id='<id>',
)

res = s.commerce.update_commerce_location(req, operations.UpdateCommerceLocationSecurity(
    jwt="<YOUR_API_KEY_HERE>",
))

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateCommerceLocationRequest](../../models/operations/updatecommercelocationrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.UpdateCommerceLocationSecurity](../../models/operations/updatecommercelocationsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.UpdateCommerceLocationResponse](../../models/operations/updatecommercelocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
