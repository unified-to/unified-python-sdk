# Inventory
(*inventory*)

### Available Operations

* [create_commerce_inventory](#create_commerce_inventory) - Create an inventory
* [get_commerce_inventory](#get_commerce_inventory) - Retrieve an inventory
* [list_commerce_inventories](#list_commerce_inventories) - List all inventories
* [patch_commerce_inventory](#patch_commerce_inventory) - Update an inventory
* [remove_commerce_inventory](#remove_commerce_inventory) - Remove an inventory
* [update_commerce_inventory](#update_commerce_inventory) - Update an inventory

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

res = s.inventory.create_commerce_inventory(req, operations.CreateCommerceInventorySecurity(
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

res = s.inventory.get_commerce_inventory(req, operations.GetCommerceInventorySecurity(
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

res = s.inventory.list_commerce_inventories(req, operations.ListCommerceInventoriesSecurity(
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

res = s.inventory.patch_commerce_inventory(req, operations.PatchCommerceInventorySecurity(
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

res = s.inventory.remove_commerce_inventory(req, operations.RemoveCommerceInventorySecurity(
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

res = s.inventory.update_commerce_inventory(req, operations.UpdateCommerceInventorySecurity(
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
