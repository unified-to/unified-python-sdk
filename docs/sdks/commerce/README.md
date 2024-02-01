# Commerce
(*commerce*)

### Available Operations

* [create_commerce_collection](#create_commerce_collection) - Create a collection
* [create_commerce_inventory](#create_commerce_inventory) - Create an inventory
* [create_commerce_item](#create_commerce_item) - Create an item/product
* [create_commerce_location](#create_commerce_location) - Create a location
* [get_commerce_collection](#get_commerce_collection) - Retrieve a collection
* [get_commerce_inventory](#get_commerce_inventory) - Retrieve an inventory
* [get_commerce_item](#get_commerce_item) - Retrieve an item/product
* [get_commerce_location](#get_commerce_location) - Retrieve a location
* [list_commerce_collections](#list_commerce_collections) - List all collections
* [list_commerce_inventories](#list_commerce_inventories) - List all inventories
* [list_commerce_items](#list_commerce_items) - List all items/products
* [list_commerce_locations](#list_commerce_locations) - List all locations
* [patch_commerce_collection](#patch_commerce_collection) - Update a collection
* [patch_commerce_inventory](#patch_commerce_inventory) - Update an inventory
* [patch_commerce_item](#patch_commerce_item) - Update an item/product
* [patch_commerce_location](#patch_commerce_location) - Update a location
* [remove_commerce_collection](#remove_commerce_collection) - Remove a collection
* [remove_commerce_inventory](#remove_commerce_inventory) - Remove an inventory
* [remove_commerce_item](#remove_commerce_item) - Remove an item/product
* [remove_commerce_location](#remove_commerce_location) - Remove a location
* [update_commerce_collection](#update_commerce_collection) - Update a collection
* [update_commerce_inventory](#update_commerce_inventory) - Update an inventory
* [update_commerce_item](#update_commerce_item) - Update an item/product
* [update_commerce_location](#update_commerce_location) - Update a location

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

res = s.commerce.create_commerce_collection(req)

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

## create_commerce_inventory

Create an inventory

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

req = operations.CreateCommerceInventoryRequest(
    commerce_inventory=shared.CommerceInventory(
        available=5165.08,
        raw={
            'key': 'string',
        },
    ),
    connection_id='string',
)

res = s.commerce.create_commerce_inventory(req)

if res.commerce_inventory is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateCommerceInventoryRequest](../../models/operations/createcommerceinventoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateCommerceInventoryResponse](../../models/operations/createcommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_commerce_item

Create an item/product

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

req = operations.CreateCommerceItemRequest(
    commerce_item=shared.CommerceItem(
        media=[
            shared.CommerceItemMedia(
                url='http://loud-minister.name',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
        variants=[
            shared.CommerceItemVariant(
                media=[
                    shared.CommerceItemMedia(
                        url='http://other-external.info',
                    ),
                ],
                name='string',
                options=[
                    shared.CommerceItemOption(
                        id='<ID>',
                        name='string',
                        values=[
                            'string',
                        ],
                    ),
                ],
                prices=[
                    shared.CommerceItemPrice(
                        price=3330.74,
                    ),
                ],
                tags=[
                    'string',
                ],
            ),
        ],
    ),
    connection_id='string',
)

res = s.commerce.create_commerce_item(req)

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateCommerceItemRequest](../../models/operations/createcommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


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
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.CreateCommerceLocationRequest(
    commerce_location=shared.CommerceLocation(
        address=shared.PropertyCommerceLocationAddress(),
        name='string',
        raw={
            'key': 'string',
        },
    ),
    connection_id='string',
)

res = s.commerce.create_commerce_location(req)

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateCommerceLocationRequest](../../models/operations/createcommercelocationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


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

res = s.commerce.get_commerce_collection(req)

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

## get_commerce_inventory

Retrieve an inventory

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetCommerceInventoryRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.commerce.get_commerce_inventory(req)

if res.commerce_inventory is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCommerceInventoryRequest](../../models/operations/getcommerceinventoryrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetCommerceInventoryResponse](../../models/operations/getcommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_commerce_item

Retrieve an item/product

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetCommerceItemRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.commerce.get_commerce_item(req)

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCommerceItemRequest](../../models/operations/getcommerceitemrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetCommerceLocationRequest(
    connection_id='string',
    fields=[
        'string',
    ],
    id='<ID>',
)

res = s.commerce.get_commerce_location(req)

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetCommerceLocationRequest](../../models/operations/getcommercelocationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


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

res = s.commerce.list_commerce_collections(req)

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

## list_commerce_inventories

List all inventories

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

req = operations.ListCommerceInventoriesRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.commerce.list_commerce_inventories(req)

if res.commerce_inventories is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListCommerceInventoriesRequest](../../models/operations/listcommerceinventoriesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ListCommerceInventoriesResponse](../../models/operations/listcommerceinventoriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_commerce_items

List all items/products

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

req = operations.ListCommerceItemsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.commerce.list_commerce_items(req)

if res.commerce_items is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListCommerceItemsRequest](../../models/operations/listcommerceitemsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


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
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListCommerceLocationsRequest(
    connection_id='string',
    fields=[
        'string',
    ],
)

res = s.commerce.list_commerce_locations(req)

if res.commerce_locations is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListCommerceLocationsRequest](../../models/operations/listcommercelocationsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


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

res = s.commerce.patch_commerce_collection(req)

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

## patch_commerce_inventory

Update an inventory

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

req = operations.PatchCommerceInventoryRequest(
    commerce_inventory=shared.CommerceInventory(
        available=615.23,
        raw={
            'key': 'string',
        },
    ),
    connection_id='string',
    id='<ID>',
)

res = s.commerce.patch_commerce_inventory(req)

if res.commerce_inventory is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchCommerceInventoryRequest](../../models/operations/patchcommerceinventoryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PatchCommerceInventoryResponse](../../models/operations/patchcommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_commerce_item

Update an item/product

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

req = operations.PatchCommerceItemRequest(
    commerce_item=shared.CommerceItem(
        media=[
            shared.CommerceItemMedia(
                url='http://frank-galley.biz',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
        variants=[
            shared.CommerceItemVariant(
                media=[
                    shared.CommerceItemMedia(
                        url='http://irresponsible-reason.biz',
                    ),
                ],
                name='string',
                options=[
                    shared.CommerceItemOption(
                        id='<ID>',
                        name='string',
                        values=[
                            'string',
                        ],
                    ),
                ],
                prices=[
                    shared.CommerceItemPrice(
                        price=4506.62,
                    ),
                ],
                tags=[
                    'string',
                ],
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.commerce.patch_commerce_item(req)

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PatchCommerceItemRequest](../../models/operations/patchcommerceitemrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


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
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.PatchCommerceLocationRequest(
    commerce_location=shared.CommerceLocation(
        address=shared.PropertyCommerceLocationAddress(),
        name='string',
        raw={
            'key': 'string',
        },
    ),
    connection_id='string',
    id='<ID>',
)

res = s.commerce.patch_commerce_location(req)

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchCommerceLocationRequest](../../models/operations/patchcommercelocationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


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

res = s.commerce.remove_commerce_collection(req)

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

## remove_commerce_inventory

Remove an inventory

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveCommerceInventoryRequest(
    connection_id='string',
    id='<ID>',
)

res = s.commerce.remove_commerce_inventory(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveCommerceInventoryRequest](../../models/operations/removecommerceinventoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RemoveCommerceInventoryResponse](../../models/operations/removecommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_commerce_item

Remove an item/product

### Example Usage

```python
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveCommerceItemRequest(
    connection_id='string',
    id='<ID>',
)

res = s.commerce.remove_commerce_item(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RemoveCommerceItemRequest](../../models/operations/removecommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


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
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.RemoveCommerceLocationRequest(
    connection_id='string',
    id='<ID>',
)

res = s.commerce.remove_commerce_location(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveCommerceLocationRequest](../../models/operations/removecommercelocationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


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

res = s.commerce.update_commerce_collection(req)

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

## update_commerce_inventory

Update an inventory

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

req = operations.UpdateCommerceInventoryRequest(
    commerce_inventory=shared.CommerceInventory(
        available=9360.02,
        raw={
            'key': 'string',
        },
    ),
    connection_id='string',
    id='<ID>',
)

res = s.commerce.update_commerce_inventory(req)

if res.commerce_inventory is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateCommerceInventoryRequest](../../models/operations/updatecommerceinventoryrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.UpdateCommerceInventoryResponse](../../models/operations/updatecommerceinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_commerce_item

Update an item/product

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

req = operations.UpdateCommerceItemRequest(
    commerce_item=shared.CommerceItem(
        media=[
            shared.CommerceItemMedia(
                url='https://aggressive-major-league.org',
            ),
        ],
        name='string',
        raw={
            'key': 'string',
        },
        tags=[
            'string',
        ],
        variants=[
            shared.CommerceItemVariant(
                media=[
                    shared.CommerceItemMedia(
                        url='https://reasonable-cast.biz',
                    ),
                ],
                name='string',
                options=[
                    shared.CommerceItemOption(
                        id='<ID>',
                        name='string',
                        values=[
                            'string',
                        ],
                    ),
                ],
                prices=[
                    shared.CommerceItemPrice(
                        price=8467.25,
                    ),
                ],
                tags=[
                    'string',
                ],
            ),
        ],
    ),
    connection_id='string',
    id='<ID>',
)

res = s.commerce.update_commerce_item(req)

if res.commerce_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateCommerceItemRequest](../../models/operations/updatecommerceitemrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


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
import dateutil.parser
import unified_to
from unified_to.models import operations, shared

s = unified_to.UnifiedTo(
    security=shared.Security(
        jwt="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.UpdateCommerceLocationRequest(
    commerce_location=shared.CommerceLocation(
        address=shared.PropertyCommerceLocationAddress(),
        name='string',
        raw={
            'key': 'string',
        },
    ),
    connection_id='string',
    id='<ID>',
)

res = s.commerce.update_commerce_location(req)

if res.commerce_location is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateCommerceLocationRequest](../../models/operations/updatecommercelocationrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.UpdateCommerceLocationResponse](../../models/operations/updatecommercelocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
